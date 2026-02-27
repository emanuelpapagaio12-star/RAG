import pypdf

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = pypdf.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

if __name__ == "__main__":
    pdf_path = "De la Teoría a la Práctica_ Diseño, Implementación y Optimización de Sistemas RAG.pdf"
    text = extract_text_from_pdf(pdf_path)
    with open("extracted_text.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("Text extracted successfully to extracted_text.txt")
