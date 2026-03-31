import os
import base64
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(BASE_DIR, "brand2.png")
OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY")
CHROMA_PATH = os.path.join(BASE_DIR, "chroma_db")

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception: return None

def load_css(file_name):
    with open(file_name) as f:
        import streamlit as st
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)