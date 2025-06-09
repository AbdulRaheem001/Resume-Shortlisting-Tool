import PyPDF2
import os

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text.strip()

def extract_text_from_txt(txt_path):
    """Extract text from a text file."""
    with open(txt_path, "r", encoding="utf-8") as file:
        return file.read().strip()

def extract_text(file_path):
    """Extract text from a file based on its extension."""
    _, ext = os.path.splitext(file_path)
    if ext.lower() == '.pdf':
        return extract_text_from_pdf(file_path)
    elif ext.lower() == '.txt':
        return extract_text_from_txt(file_path)
    else:
        raise ValueError("Unsupported file type: {}".format(ext))