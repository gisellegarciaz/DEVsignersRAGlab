# rag_engine.py
import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader, BSHTMLLoader 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import CHROMA_PATH, OPENROUTER_KEY

@st.cache_resource
def get_embeddings():
    return HuggingFaceEmbeddings(model_name="mixedbread-ai/mxbai-embed-large-v1")

def process_file(uploaded_file):
    # Processa arquivos PDF ou HTML para o banco vetorial
    ext = os.path.splitext(uploaded_file.name)[1].lower()
    temp_path = os.path.join(os.path.dirname(__file__), f"temp{ext}")
    
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    if ext == ".pdf":
        loader = PyPDFLoader(temp_path)
    elif ext == ".html":
        # BSHTMLLoader limpa as tags HTML e extrai o título
        loader = BSHTMLLoader(temp_path)
    else:
        st.error(f"Formato {ext} não suportado.")
        return None

    data = loader.load()
    
    # Print de depuração 
    # print(f"Documentos: {len(data)} | Metadados: {data[0].metadata}")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(data)
    
    vector_db = Chroma.from_documents(documents=chunks, embedding=get_embeddings())
    return vector_db.as_retriever(
    search_type="similarity_score_threshold", 
    search_kwargs={"k": 3, "score_threshold": 0.7}
)

@st.cache_resource
def init_wiki_rag():
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=get_embeddings())
    return db.as_retriever(search_kwargs={"k": 3})

def get_llm():
    return ChatOpenAI(
        model="openai/gpt-4o-mini", 
        api_key=OPENROUTER_KEY, 
        base_url="https://openrouter.ai/api/v1", 
        streaming=True,
        temperature=0.2
    )