# app.py

import streamlit as st
from PyPDF2 import PdfReader
import os
from sentence_transformers import SentenceTransformer
import faiss
from transformers import pipeline
import tempfile

# Load embedding model and QA model
embedder = SentenceTransformer("all-MiniLM-L6-v2")
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Function: Extract text from uploaded PDF or TXT
def extract_text(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
    else:
        text = uploaded_file.read().decode("utf-8")
    return text

# Function: Chunk text for embedding
def chunk_text(text, max_length=500):
    sentences = text.split('. ')
    chunks, chunk = [], ""
    for sentence in sentences:
        if len(chunk) + len(sentence) < max_length:
            chunk += sentence + ". "
        else:
            chunks.append(chunk.strip())
            chunk = sentence + ". "
    chunks.append(chunk.strip())
    return chunks

# Function: Embed and build FAISS index
def build_faiss_index(chunks):
    embeddings = embedder.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index, embeddings, chunks

# Function: Retrieve relevant context
def retrieve_context(query, index, chunks, embeddings, k=3):
    query_embedding = embedder.encode([query])
    D, I = index.search(query_embedding, k)
    return " ".join([chunks[i] for i in I[0]])

# Function: Ask question using QA model
def ask_question(context, question):
    result = qa_pipeline(question=question, context=context)
    return result["answer"]

# Streamlit UI
st.title("📄 Resume Q&A with RAG")

uploaded_file = st.file_uploader("Upload Resume (PDF or TXT)", type=["pdf", "txt"])
if uploaded_file:
    resume_text = extract_text(uploaded_file)
    chunks = chunk_text(resume_text)
    index, embeddings, chunk_data = build_faiss_index(chunks)
    st.success("Resume uploaded and indexed successfully.")

    question = st.text_input("Ask a question about the resume:")
    if question:
        context = retrieve_context(question, index, chunk_data, embeddings)
        answer = ask_question(context, question)
        st.markdown(f"**Answer:** {answer}")
