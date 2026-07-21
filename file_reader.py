import os
from pypdf import PdfReader
from docx import Document


def read_file(path):

    if path.endswith(".pdf"):
        text = ""

        reader = PdfReader(path)

        for page in reader.pages:
            text += page.extract_text() or ""

        return text


    elif path.endswith(".docx"):
        doc = Document(path)

        text = ""

        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"

        return text


    elif path.endswith(".txt"):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()


    else:
        return "Не поддържам този тип файл."