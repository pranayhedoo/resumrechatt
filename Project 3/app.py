import streamlit as st
import uuid
from rag_chain import create_rag_chain
from utils import extract_text_from_pdf
from db import save_chat, get_chat_history, list_sessions

st.set_page_config(page_title="AI Resume Chatbot", layout="wide")

st.title("📄 AI-Powered Resume Chatbot")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar: Session and Upload
st.sidebar.header("Upload Resume & Sessions")
uploaded_file = st.sidebar.file_uploader("Upload PDF Resume", type=["pdf"])
if uploaded_file:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())
    text = extract_text_from_pdf("temp_resume.pdf")
    st.session_state.rag_chain = create_rag_chain(text)
    st.success("Resume uploaded and processed!")

# Chat history list
if st.sidebar.button("Refresh Sessions"):
    st.rerun()

sessions = list_sessions()
for session in sessions:
    if st.sidebar.button(f"📂 {session[:8]}..."):
        st.session_state.session_id = session
        st.session_state.chat_history = get_chat_history(session)
        st.rerun()

# Chat UI
st.subheader("💬 Chat with Resume")

for message, response in st.session_state.chat_history:
    st.chat_message("user").write(message)
    st.chat_message("ai").write(response)

prompt = st.chat_input("Ask something about the resume...")
if prompt and st.session_state.rag_chain:
    response = st.session_state.rag_chain.run(prompt)
    st.chat_message("user").write(prompt)
    st.chat_message("ai").write(response)

    st.session_state.chat_history.append((prompt, response))
    save_chat(st.session_state.session_id, prompt, response)
