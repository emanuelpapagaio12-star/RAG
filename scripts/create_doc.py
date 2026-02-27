from odf.opendocument import OpenDocumentText
from odf.text import P, H, Span
from odf.draw import Frame, Image
from odf.teletype import addTextToElement
import os

def create_initial_doc(filename):
    textdoc = OpenDocumentText()
    
    # Title
    h = H(outlinelevel=1, text="Documentación del Sistema RAG")
    textdoc.text.addElement(h)
    
    # Introduction
    p = P(text="Este documento detalla el proceso de creación de un sistema de Generación Aumentada por Recuperación (RAG) basado en un informe de investigación.")
    textdoc.text.addElement(p)
    
    # User Request
    p = P()
    p.setAttribute("stylename", "Heading_2")
    addTextToElement(p, "Solicitud del Usuario")
    textdoc.text.addElement(p)
    
    p = P(text="El usuario solicitó un sistema RAG utilizando la información de un PDF en la carpeta y una documentación completa en formato .odt, incluyendo imágenes y capturas.")
    textdoc.text.addElement(p)
    
    # Installation Process
    h = H(outlinelevel=2, text="Instalación de Dependencias")
    textdoc.text.addElement(h)
    p = P(text="Para el desarrollo del sistema, se instalaron las siguientes librerías:")
    textdoc.text.addElement(p)
    
    dependencies = ["langchain", "langchain-community", "faiss-cpu", "sentence-transformers", "pypdf", "odfpy"]
    for dep in dependencies:
        p = P(text=f"- {dep}")
        textdoc.text.addElement(p)
    
    textdoc.save(filename)
    print(f"Documento inicial creado: {filename}")

if __name__ == "__main__":
    create_initial_doc("Documentacion_RAG.odt")
