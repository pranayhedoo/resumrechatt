import PyPDF2

def parse_resume(file):
    if file.name.endswith(".pdf"):
        pdf = PyPDF2.PdfReader(file)
        text = "".join(page.extract_text() for page in pdf.pages)
        return text
    else:
        return file.read().decode("utf-8")
