import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import CHROMA_PATH, OPENROUTER_KEY

@st.cache_resource
def get_embeddings():
    return HuggingFaceEmbeddings(model_name="mixedbread-ai/mxbai-embed-large-v1")

def process_pdf(uploaded_file):
    temp_path = os.path.join(os.path.dirname(__file__), "temp.pdf")
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    loader = PyPDFLoader(temp_path)
    chunks = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100).split_documents(loader.load())
    
    vector_db = Chroma.from_documents(documents=chunks, embedding=get_embeddings())
    return vector_db.as_retriever(search_kwargs={"k": 3})

@st.cache_resource
def init_wiki_rag():
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=get_embeddings())
    return db.as_retriever(search_kwargs={"k": 3})

def get_llm():
    return ChatOpenAI(
        model="openai/gpt-4o-mini", 
        api_key=OPENROUTER_KEY, 
        base_url="https://openrouter.ai/api/v1", 
        streaming=True
    )