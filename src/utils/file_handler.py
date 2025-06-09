import os

def upload_file(file):
    """
    Save the uploaded file to a designated directory.
    """
    upload_folder = 'uploads'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    file_path = os.path.join(upload_folder, file.name)
    with open(file_path, 'wb') as f:
        f.write(file.getbuffer())
    return file_path

def read_text_file(file_path):
    """
    Read text from a file and return it as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def read_pdf_file(file_path):
    """
    Read text from a PDF file and return it as a string.
    """
    import PyPDF2
    text = ''
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + '\n'
    return text