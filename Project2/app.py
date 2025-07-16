import streamlit as st
from utils import parse_resume
from rag_engine import get_response
from memory import save_chat, load_chat

st.set_page_config(page_title="Resume Q&A Chatbot")
st.title("📄 Resume Q&A Chatbot")

# Upload
uploaded_file = st.file_uploader("Upload Resume (PDF or .txt)", type=["pdf", "txt"])
if uploaded_file:
    resume_text = parse_resume(uploaded_file)
    st.session_state['resume'] = resume_text
    st.success("Resume uploaded successfully.")

# Chat
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

query = st.text_input("Ask a question about the resume:")

if query and 'resume' in st.session_state:
    response = get_response(query, st.session_state['resume'], st.session_state['chat_history'])
    st.session_state['chat_history'].append((query, response))
    save_chat(query, response)

# Display Chat History
st.subheader("🗂️ Chat History")
for q, r in st.session_state['chat_history']:
    st.markdown(f"**You:** {q}\n\n**Bot:** {r}")
