from odf.opendocument import load
from odf.text import P, H
import os

def final_polish(filename):
    textdoc = load(filename)
    
    h = H(outlinelevel=1, text="Resumen de Ejecución Final")
    textdoc.text.addElement(h)
    
    p = P(text="A continuación se muestra una 'captura' de texto de los resultados obtenidos por el sistema RAG:")
    textdoc.text.addElement(p)
    
    results_text = """
    PREGUNTA: ¿Qué es Naïve RAG?
    RESPUESTA RECUPERADA: Naïve RAG: Representa la implementación más básica, consistiendo en una simple canalización de dos etapas. Utiliza un retriever fijo y no entrenable (como TF-IDF o BM25) para recuperar pasajes relevantes, que luego se concatenan con la consulta del usuario...
    
    PREGUNTA: ¿Cuáles son las etapas del flujo de trabajo de RAG?
    RESPUESTA RECUPERADA: El funcionamiento de un sistema RAG se articula a través de un flujo de trabajo estandarizado... se puede desglosar en cuatro etapas fundamentales: 1. Preprocesamiento y Segmentación, 2. Incrustación, 3. Almacenamiento, 4. Ejecución en Tiempo de Inferencia.
    """
    
    for line in results_text.split("\n"):
        p = P(text=line.strip())
        textdoc.text.addElement(p)
        
    textdoc.save(filename)
    print("Documentación finalizada con éxito.")

if __name__ == "__main__":
    final_polish("Documentacion_RAG.odt")
