import docx2txt
from PyPDF2 import PdfReader
def extract_text(filepath):
    if filepath.lower().endswith(".pdf"):
        reader = PdfReader(filepath)
        return " ".join(page.extract_text() or "" for page in reader.pages)
    elif filepath.lower().endswith(".docx"):
        return docx2txt.process(filepath)
    else:
        raise ValueError("Unsupported file type. Use PDF or DOCX.")
