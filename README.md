# TCS-Chatbot-RAG
A PDF-based TCS Chatbot using Retrieval-Augmented Generation (RAG), FAISS vector search, Hugging Face embeddings, Gemini API, and Flask to answer questions strictly from the TCS document.
# TCS Chatbot using RAG

A PDF-based chatbot that answers user questions using information retrieved from a TCS document.

## Project Overview

This project uses Retrieval-Augmented Generation (RAG) to retrieve relevant content from a PDF and generate answers based only on the available document context. If the answer is not present in the document, the chatbot returns a predefined fallback message.

## Features

- PDF-based question answering
- Semantic search using FAISS
- Text embeddings using Hugging Face Sentence Transformers
- Gemini API for answer generation
- Flask backend with an HTML chat interface
- Document-grounded answers with a fallback for missing information

## Technologies Used

- Python
- Flask
- LangChain
- FAISS
- Hugging Face Sentence Transformers
- Google Gemini API
- HTML, CSS, JavaScript
- PyPDF

## Project Structure

```text
TCS-Chatbot-RAG/
├── app.py
├── batchjob.py
├── templates/
│   └── index.html
├── documents/       # Local PDF files; not committed
├── tcs_doc_index/   # Local FAISS index; not committed
├── .env             # API key; not committed
├── .gitignore
└── README.md
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Arya-gunji/TCS-Chatbot-RAG.git
cd TCS-Chatbot-RAG
```

### 2. Create and activate a virtual environment

```bash
python -m venv ChatBotEnv
```

Windows PowerShell:

```powershell
.\ChatBotEnv\Scripts\Activate.ps1
```

### 3. Install dependencies

Install the required packages used by the project, such as Flask, LangChain Community, LangChain Hugging Face, FAISS CPU, PyPDF, Sentence Transformers, Google GenAI, and python-dotenv.

### 4. Configure the API key

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

Replace the placeholder with your own API key. Never commit your actual API key to GitHub.

### 5. Prepare the PDF and FAISS index

Place an authorized PDF in the `documents/` folder and run:

```bash
python batchjob.py
```

This prepares the vector index used by the chatbot. The PDF and generated index are stored locally.

### 6. Start the application

```bash
python app.py
```

Open the local URL displayed in the terminal, usually `http://127.0.0.1:5000`.

## Expected Behavior

- Answers questions using relevant content from the configured PDF.
- Avoids answering from general knowledge.
- Returns `I could not find the answer in the TCS document.` when the document does not contain sufficient information.

## Security

- Keep `.env` and API keys private.
- Do not upload confidential or copyrighted documents without permission.
- Keep local virtual environments and generated index files out of version control.

## Author

**Arya Gunji**

GitHub: [Arya-gunji](https://github.com/Arya-gunji)