import os
import glob
from rag_system import RAGSystem

def main():
    # 1. Buscar archivos PDF disponibles
    pdfs = glob.glob("*.pdf")
    
    if not pdfs:
        print("No se encontraron archivos PDF en la carpeta actual.")
        return

    print("\n--- Selecciona un documento ---")
    for i, pdf in enumerate(pdfs):
        print(f"{i + 1}. {pdf}")
    
    try:
        choice = int(input("\nIntroduce el número del documento: ")) - 1
        if choice < 0 or choice >= len(pdfs):
            print("Selección no válida.")
            return
        selected_pdf = pdfs[choice]
    except ValueError:
        print("Por favor, introduce un número.")
        return

    # 2. Inicializar el sistema RAG con el documento elegido
    print(f"\nProcesando '{selected_pdf}'... Esto puede tardar un momento.")
    rag = RAGSystem(selected_pdf)
    rag.ingest()
    print("\n¡Sistema listo! Ya puedes hacer tus preguntas.")

    # 3. Bucle de chat
    while True:
        query = input("\nPregunta (o escribe 'salir' para terminar): ")
        
        if query.lower() in ["salir", "exit", "quit"]:
            print("Cerrando el sistema...")
            break
        
        if not query.strip():
            continue

        print("\nBuscando en el documento...")
        results = rag.query(query)
        
        print("\n--- Resultados encontrados ---")
        if not results:
            print("No se encontró información relevante.")
        else:
            for i, doc in enumerate(results):
                print(f"\n[Fragmento {i+1} - Página {doc.metadata.get('page', 'Desconocida')}]:")
                print("-" * 30)
                print(doc.page_content)
                print("-" * 30)

if __name__ == "__main__":
    main()
