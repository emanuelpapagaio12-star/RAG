import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

class RAGSystem:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.vector_db = None
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    def ingest(self):
        print(f"Loading PDF: {self.pdf_path}")
        loader = PyPDFLoader(self.pdf_path)
        documents = loader.load()
        
        print("Splitting documents into chunks...")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = text_splitter.split_documents(documents)
        
        print(f"Creating vector database with {len(chunks)} chunks...")
        self.vector_db = FAISS.from_documents(chunks, self.embeddings)
        print("Vector database created successfully.")
    
    def query(self, user_query, k=3):
        if not self.vector_db:
            return "Error: Database not ingested."
        
        print(f"Searching for: {user_query}")
        docs = self.vector_db.similarity_search(user_query, k=k)
        return docs

if __name__ == "__main__":
    pdf_file = "De la Teoría a la Práctica_ Diseño, Implementación y Optimización de Sistemas RAG.pdf"
    rag = RAGSystem(pdf_file)
    rag.ingest()
    
    # Test query
    query_text = "¿Qué es Naïve RAG?"
    results = rag.query(query_text)
    
    print("\n--- Resultados de la Recuperación ---")
    for i, doc in enumerate(results):
        print(f"\nResultado {i+1}:")
        print(doc.page_content)
