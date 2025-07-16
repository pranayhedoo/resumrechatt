import fitz  # PyMuPDF
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("AIzaSyBaCf3gb2i9NXjUL5Q3Be2qzQoQRvu24Sk")

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    # os.environ["OPENAI_API_KEY"] = "AIzaSyBaCf3gb2i9NXjUL5Q3Be2qzQoQRvu24Sk"
    for page in doc:
        text += page.get_text()
    return text
 