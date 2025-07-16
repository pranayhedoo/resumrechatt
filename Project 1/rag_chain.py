# from langchain.chat_models import ChatOpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document


# import uuid 

def create_rag_chain(resume_text):
    docs = [Document(page_content=resume_text)]
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    embedding = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(chunks, embedding)

    llm = ChatOpenAI(model="gpt-4", temperature=0)

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        return_source_documents=True
    )
    return chain
