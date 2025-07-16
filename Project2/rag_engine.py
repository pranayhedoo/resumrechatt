from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

def get_response(question, resume_text, history):
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(resume_text)

    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.from_texts(chunks, embeddings)
    retriever = vectordb.as_retriever()

    llm = OpenAI()
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain.run(question)
