from PIL import Image
import pytesseract
import fitz  # PyMuPDF
import pandas as pd
from docx import Document
import tempfile

def extract_text(file):
    file_type = file.type
    if file_type in ["image/jpeg", "image/png"]:
        image = Image.open(file)
        return pytesseract.image_to_string(image)
    elif file_type == "application/pdf":
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(file.read())
            doc = fitz.open(tmp_file.name)
            text = ""
            for page in doc:
                text += page.get_text()
            return text
    elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = Document(file)
        return "\n".join([para.text for para in doc.paragraphs])
    elif file_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        df = pd.read_excel(file)
        return df.to_string(index=False)
    else:
        return "Unsupported file type."
