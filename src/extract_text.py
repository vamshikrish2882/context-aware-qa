# src/extract_text.py

import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

if __name__ == "__main__":
    path = "../data/ceo-guide-to-ai-revolution.pdf"
    text = extract_text_from_pdf(path)
    
    # Save to file for QA input
    with open("bcg_ai_guide.txt", "w", encoding="utf-8") as f:
        f.write(text)
    
    print(" PDF text extracted and saved.")
