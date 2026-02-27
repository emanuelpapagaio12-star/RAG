# 🧠 RAG Intelligence System

A high-performance **Retrieval-Augmented Generation (RAG)** application designed to extract and query knowledge from PDF documents with semantic precision.

Built with **Streamlit**, **LangChain**, and **FAISS**, this system provides a seamless interface for interacting with your data locally and securely.

## ✨ Features

- **🚀 Instant Indexing**: Upload any PDF and index its content in seconds using FAISS.
- **🔍 Semantic Search**: Uses state-of-the-art vector embeddings to find the most relevant context.
- **💬 Interactive Chat**: Ask complex questions and get grounded answers based strictly on the provided document.
- **🛡️ Privacy First**: All processing is done locally; your documents never leave your environment.
- **💎 Premium UI**: A modern, dark-themed interface designed for the best user experience.

## 🛠️ Tech Stack

- **Streamlit**: For the interactive web interface.
- **LangChain**: To orchestrate the RAG pipeline.
- **FAISS**: For efficient vector storage and similarity search.
- **Sentence-Transformers**: To generate high-quality text embeddings.
- **PyPDF**: For robust PDF text extraction.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- [Git](https://git-scm.com/)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/emanuelpapagaio12-star/RAG.git
   cd RAG
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run rag_web_app.py
   ```

## 📁 Project Structure

```text
.
├── rag_web_app.py      # Main Streamlit application
├── rag_system.py       # Core RAG engine logic
├── requirements.txt    # Project dependencies
├── docs/               # Landing page for GitHub Pages
└── scripts/            # Utility scripts for development
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
*Created by [emanuelpapagaio12-star](https://github.com/emanuelpapagaio12-star)*
