from odf.opendocument import load
from odf.text import P, H
import os

def update_doc_with_new_features(filename):
    if not os.path.exists(filename):
        print(f"Error: {filename} no existe.")
        return

    textdoc = load(filename)
    
    # NEW SECTION: Utility and Value
    h = H(outlinelevel=2, text="Ampliación: Utilidad y Valor del Sistema")
    textdoc.text.addElement(h)
    
    utilities = [
        "El sistema RAG implementado no es solo un buscador, sino un motor de inteligencia propia con las siguientes ventajas:",
        "- Consulta Eficiente: Permite interrogar documentos extensos sin necesidad de lectura lineal.",
        "- Reducción de Alucinaciones: Al estar anclado a documentos reales, la IA no inventa datos operativos o técnicos.",
        "- Escalabilidad: El sistema permite integrar múltiples documentos para crear una base de conocimiento corporativa o personal sólida."
    ]
    for util in utilities:
        p = P(text=util)
        textdoc.text.addElement(p)

    # NEW SECTION: Interactivity and Multi-document Support
    h = H(outlinelevel=2, text="Ampliación: Interfaz de Usuario e Interactividad")
    textdoc.text.addElement(h)
    
    interactivity = [
        "Se ha desarrollado un componente interactivo adicional para mejorar la experiencia del usuario:",
        "- Script de Chat (chat_with_pdf.py): Este script transforma el sistema en un chat interactivo.",
        "- Selección de Documentos: El sistema ahora detecta automáticamente todos los archivos PDF en el directorio y permite al usuario elegir cuál procesar.",
        "- Bucle de Pregunta-Respuesta: Permite realizar múltiples consultas seguidas sin reiniciar el proceso, manteniendo un flujo de trabajo ágil.",
        "- Metadatos de Recuperación: El sistema ahora informa no solo el contenido, sino también el número de página de donde se extrajo la información."
    ]
    for item in interactivity:
        p = P(text=item)
        textdoc.text.addElement(p)

    textdoc.save(filename)
    print(f"Documentación '{filename}' actualizada con las nuevas funciones.")

if __name__ == "__main__":
    update_doc_with_new_features("Documentacion_RAG.odt")
