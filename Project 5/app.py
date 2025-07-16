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

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)
    rag_chain = create_rag_chain(resume_text)
    st.success("✅ Resume processed successfully!")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("Ask something about the resume:")

    if user_input:
        response = rag_chain.run(user_input)
        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append(("bot", response))
        save_chat(st.session_state.session_id, "user", user_input)
        save_chat(st.session_state.session_id, "bot", response)

    for role, msg in st.session_state.chat_history:
        if role == "user":
            st.markdown(f"👤 **You**: {msg}")
        else:
            st.markdown(f"🤖 **Bot**: {msg}")

with st.sidebar:
    st.header("🕓 Chat Sessions")
    for session in list_sessions():
        if st.button(session):
            st.session_state.session_id = session
            st.session_state.chat_history = get_chat_history(session)
