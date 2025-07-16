import streamlit as st
import uuid
from rag_chain import create_rag_chain
from utils import extract_text_from_pdf
from db import init_db, save_chat, get_chat_history, list_sessions

init_db()
st.set_page_config(page_title="Smart Resume Chatbot", layout="wide")

st.title("📄 Smart Resume Chatbot")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
    st.session_state.chat_history = []

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)
    st.session_state.rag_chain = create_rag_chain(resume_text)
    st.success("Resume uploaded and processed.")

if "rag_chain" in st.session_state:
    user_input = st.text_input("Ask a question about the resume")

    if user_input:
        chain = st.session_state.rag_chain
        chat_history = st.session_state.chat_history

        result = chain({"question": user_input, "chat_history": chat_history})
        answer = result["answer"]

        st.chat_message("user").write(user_input)
        st.chat_message("assistant").write(answer)

        st.session_state.chat_history.append((user_input, answer))

        # Save to DB
        save_chat(st.session_state.session_id, "user", user_input)
        save_chat(st.session_state.session_id, "assistant", answer)

with st.sidebar:
    st.header("🗂️ Chat History")
    for session in list_sessions():
        if st.button(session):
            st.session_state.session_id = session
            history = get_chat_history(session)
            st.session_state.chat_history = history
            st.rerun()
