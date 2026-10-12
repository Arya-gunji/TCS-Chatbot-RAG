from flask import Flask, request, jsonify, render_template
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from google import genai
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv()

app = Flask(__name__)

NOT_FOUND = "I could not find the answer in the TCS document."

# Load embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)

# Load existing FAISS index
vector_store = FAISS.load_local(
    "tcs_doc_index",
    embedding_model,
    allow_dangerous_deserialization=True
)

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is missing. Check your .env file."
    )

client = genai.Client(api_key=api_key)


# Gemini request with retry
def generate_with_retry(prompt):
    for attempt in range(3):
        try:
            return client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )

        except Exception as error:
            print("Gemini error:", error)

            if attempt == 2:
                raise

            wait_seconds = 2 * (attempt + 1)
            print(
                f"Retrying in {wait_seconds} seconds..."
            )
            time.sleep(wait_seconds)


# Home page
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


# TCS chatbot API
@app.route("/tcs", methods=["POST"])
def tcs_chatbot_api():

    data = request.get_json(silent=True) or {}
    question = data.get("tcs_question", "").strip()

    if not question:
        return jsonify({
            "response": "Please enter a question."
        }), 400

    try:
        # Retrieve relevant PDF chunks
        results = vector_store.similarity_search_with_score(
            question,
            k=5
        )

        if not results:
            return jsonify({"response": NOT_FOUND})

        context_parts = []

        for document, score in results:
            context_parts.append(document.page_content)

        context_text = "\n\n".join(context_parts)

        # Check whether the PDF contains the answer
        relevance_prompt = f"""
You are a strict TCS PDF answer checker.

Use ONLY the PDF context below.

PDF CONTEXT:
{context_text}

QUESTION:
{question}

Can this question be answered using the supplied PDF context?

Reply with exactly YES or NO.

Reply YES only if the context contains information
that answers the question.

Reply NO if the information is missing, unrelated,
or insufficient.

Do not use outside knowledge.
"""

        check = generate_with_retry(relevance_prompt)

        relevance = (check.text or "").strip().upper()

        if relevance != "YES":
            return jsonify({"response": NOT_FOUND})

        # Generate an answer using only the PDF context
        answer_prompt = f"""
You are a TCS PDF question-answering assistant.

Answer using ONLY the PDF context provided below.

Rules:
1. Do not use general knowledge or outside information.
2. Do not guess or invent facts.
3. If the answer is not available in the context,
   reply exactly:
   {NOT_FOUND}
4. Give a clear, direct answer.

PDF CONTEXT:
{context_text}

QUESTION:
{question}

ANSWER:
"""

        response = generate_with_retry(answer_prompt)

        answer = (response.text or "").strip()

        if not answer:
            answer = NOT_FOUND

        return jsonify({"response": answer})

    except Exception as error:
        print("Chatbot error:", error)

        return jsonify({
            "response": (
                "Gemini service is temporarily unavailable. "
                "Please try again later."
            )
        }), 503


if __name__ == "__main__":
    app.run(debug=True)