import pdfplumber
import os

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        os.environ["OPENAI_API_KEY"] = "AIzaSyBaCf3gb2i9NXjUL5Q3Be2qzQoQRvu24Sk"
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()
