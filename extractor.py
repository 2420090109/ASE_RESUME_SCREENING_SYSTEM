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
import re
SKILL_KEYWORDS = [
    "python", "java", "sql", "flask", "django", "react", "docker",
    "kubernetes", "git", "machine learning", "nlp", "aws", "tensorflow",
    "pandas", "numpy", "html", "css", "javascript", "c++", "linux"
]
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s+.#]", " ", text)
    return re.sub(r"\s+", " ", text).strip()
def extract_skills(text):
    text = clean_text(text)
    return sorted({skill for skill in SKILL_KEYWORDS if skill in text})
