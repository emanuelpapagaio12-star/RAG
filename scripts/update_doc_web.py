from odf.opendocument import load
from odf.text import P, H
import os

def update_doc_with_web_interface(filename):
    if not os.path.exists(filename):
        print(f"Error: {filename} no existe.")
        return

    textdoc = load(filename)
    
    # NEW SECTION: Web Interface (Streamlit)
    h = H(outlinelevel=2, text="Fase 4: Desarrollo de Interfaz Web (Streamlit)")
    textdoc.text.addElement(h)
    
    web_features = [
        "Se ha implementado una capa de presentación moderna utilizando Streamlit, elevando el sistema de una herramienta de terminal a una aplicación web completa.",
        "- Interfaz Premium: Diseño visual con estética oscura (Dark Mode), degradados y estilos CSS personalizados para una experiencia de usuario profesional.",
        "- Carga Dinámica: Incorporación de un 'File Uploader' que permite subir archivos PDF directamente desde el navegador.",
        "- Procesamiento Automatizado: El sistema gestiona la carga, el guardado temporal y la indexación vectorial (ingestión) de forma transparente para el usuario.",
        "- UI de Chat Moderna: Implementación de componentes de chat nativos de Streamlit para una interacción fluida y natural.",
        "- Feedback Visual: Uso de indicadores de carga (spinners) y estados de éxito/error para guiar al usuario durante el proceso de indexación y consulta."
    ]
    for feat in web_features:
        p = P(text=feat)
        textdoc.text.addElement(p)

    # NEW SECTION: Technical Stack Update
    h = H(outlinelevel=2, text="Actualización del Stack Tecnológico")
    textdoc.text.addElement(h)
    
    stack = [
        "Con la nueva interfaz web, el ecosistema tecnológico del proyecto se consolida con:",
        "- Frontend/UI: Streamlit (Framework de aplicaciones de datos).",
        "- Gestión de Archivos: Python OS & Secrets para manejo seguro de rutas.",
        "- Dependencias: Se ha creado un archivo 'requirements.txt' para facilitar la replicación del entorno.",
        "- Servidor: Servidor web local integrado capaz de manejar múltiples peticiones concurrentes."
    ]
    for item in stack:
        p = P(text=item)
        textdoc.text.addElement(p)

    textdoc.save(filename)
    print(f"Documentación '{filename}' actualizada con la información de la interfaz web.")

if __name__ == "__main__":
    update_doc_with_web_interface("Documentacion_RAG.odt")
