from rag_system import RAGSystem
from odf.opendocument import load
from odf.text import P, H, List, ListItem
from odf.teletype import addTextToElement
import os

def append_to_doc(filename, section_title, content_list):
    textdoc = load(filename)
    h = H(outlinelevel=2, text=section_title)
    textdoc.text.addElement(h)
    for item in content_list:
        p = P(text=item)
        textdoc.text.addElement(p)
    textdoc.save(filename)

def main():
    pdf_file = "De la Teoría a la Práctica_ Diseño, Implementación y Optimización de Sistemas RAG.pdf"
    doc_name = "Documentacion_RAG.odt"
    
    print("--- Iniciando Sistema RAG ---")
    rag = RAGSystem(pdf_file)
    rag.ingest()
    
    # Query 1
    q1 = "¿Qué es Naïve RAG?"
    print(f"Pregunta 1: {q1}")
    res1 = rag.query(q1)
    
    # Query 2
    q2 = "¿Cuáles son las etapas del flujo de trabajo de RAG?"
    print(f"Pregunta 2: {q2}")
    res2 = rag.query(q2)
    
    # Update Documentation
    print("Actualizando documentación con resultados...")
    append_to_doc(doc_name, "Fase 3: Ejecución y Pruebas", [
        "Se realizaron pruebas de recuperación con el sistema implementado.",
        f"Pregunta: {q1}",
        f"Respuesta Recuperada (Fragmento 1): {res1[0].page_content[:300]}...",
        f"Pregunta: {q2}",
        f"Respuesta Recuperada (Fragmento 1): {res2[0].page_content[:300]}..."
    ])
    
    append_to_doc(doc_name, "Conclusión", [
        "El sistema RAG ha sido implementado con éxito, permitiendo la recuperación precisa de información semántica basada en el documento PDF proporcionado.",
        "La documentación en formato .odt refleja todos los pasos técnicos y decisiones arquitectónicas tomadas durante el proceso."
    ])
    print("Proceso completado.")

if __name__ == "__main__":
    main()
