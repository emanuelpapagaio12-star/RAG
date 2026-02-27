from odf.opendocument import load
from odf.text import P, H, List, ListItem
from odf.teletype import addTextToElement
import os

def append_to_doc(filename, section_title, content_list):
    textdoc = load(filename)
    
    # Section Header
    h = H(outlinelevel=2, text=section_title)
    textdoc.text.addElement(h)
    
    # Content
    for item in content_list:
        p = P(text=item)
        textdoc.text.addElement(p)
    
    textdoc.save(filename)
    print(f"Documento actualizado: {filename}")

if __name__ == "__main__":
    doc_name = "Documentacion_RAG.odt"
    
    # Phase 1: Exploration and Requirements
    append_to_doc(doc_name, "Fase 1: Exploración y Requisitos", [
        "1. Se identificó el archivo fuente: 'De la Teoría a la Práctica_ Diseño, Implementación y Optimización de Sistemas RAG.pdf'.",
        "2. Se extrajo el texto base para verificar el contenido y la estructura del informe.",
        "3. Se definió el stack tecnológico: Python, LangChain, FAISS y SentenceTransformers."
    ])
    
    # Phase 2: Architecture
    append_to_doc(doc_name, "Fase 2: Arquitectura del Sistema", [
        "El sistema sigue una arquitectura de RAG Clásico (Naïve RAG) con los siguientes componentes:",
        "- Carga de Documentos: Uso de PyPDFLoader para procesar el PDF.",
        "- Fragmentación (Chunking): División del texto en fragmentos de 500 tokens con un solapamiento de 50 para preservar el contexto.",
        "- Embeddings: Generación de vectores semánticos mediante el modelo 'all-MiniLM-L6-v2'.",
        "- Almacenamiento Vectorial: Uso de FAISS (Facebook AI Similarity Search) para una indexación y búsqueda eficiente.",
        "- Recuperación: Búsqueda por similitud de coseno para encontrar los pasajes más relevantes."
    ])
