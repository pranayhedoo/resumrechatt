from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

def create_rag_chain(texts):
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.create_documents([texts])
    
    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.from_documents(docs, embeddings)
    retriever = vectordb.as_retriever()
    
    llm = ChatOpenAI(model="gpt-4")
    llm = OpenAI(temperature=0)
    rag_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return rag_chain
