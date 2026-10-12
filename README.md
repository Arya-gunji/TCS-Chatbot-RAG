# TCS Document Chatbot Using RAG

A document-based AI chatbot that answers user questions using information retrieved from a TCS PDF document.

## Project Overview

This project uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from a PDF and generate answers based on the retrieved context. If the required information is not available in the document, the chatbot returns a predefined fallback message.

## Technologies Used

- Python
- Flask
- LangChain
- FAISS Vector Database
- Hugging Face Sentence Transformers
- Google Gemini API
- HTML, CSS, JavaScript
- PyPDF

## Key Features

- Ask questions about the configured TCS PDF.
- Retrieve relevant document chunks using FAISS similarity search.
- Generate context-based answers using Gemini.
- Avoid answering questions unsupported by the document.
- Provide a fallback message when the answer cannot be found.

## Project Structure

```text
TCS-Chatbot-RAG/
├── app.py
├── batchjob.py
├── requirements.txt
├── .gitignore
├── README.md
├── documents/
├── tcs_doc_index/
└── templates/
    └── index.html
```

## Installation and Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/Arya-gunji/TCS-Chatbot-RAG.git
   cd TCS-Chatbot-RAG
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

   Windows PowerShell:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your Gemini API key:

   ```text
   GEMINI_API_KEY=your_api_key_here
   ```

   Never upload your real API key to GitHub.

5. Ensure the required PDF document is available locally and generate the FAISS index using the project's indexing script:

   ```bash
   python batchjob.py
   ```

6. Start the Flask application:

   ```bash
   python app.py
   ```

7. Open the local URL displayed in the terminal, usually `http://127.0.0.1:5000`.

## Security and Data

The API key, private documents, and other sensitive files should not be committed to the repository. Access to the source PDF must comply with its applicable permissions.

## Future Improvements

- Improve document retrieval accuracy.
- Add source references to answers.
- Improve error handling and response time.
- Deploy the application to a suitable hosting platform.

## Author

**Arya Gunji**

GitHub: [Arya-gunji](https://github.com/Arya-gunji)