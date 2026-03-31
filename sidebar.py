# components.py
import streamlit as st
from config import get_base64_image, LOGO_PATH

def render_sidebar(process_pdf_func, init_wiki_func):
    img_base64 = get_base64_image(LOGO_PATH)
    
    with st.sidebar:

        # Header
        st.markdown(f"""
            <div class='sidebar-header'>
                <img src='data:image/png;base64,{img_base64}' width='90'>
                <div>
                    <div style='color: #f8f8f2; font-weight: bold; font-size: 1.1rem;'>Giselle Garcia</div>
                    <div style='color: #6272a4; font-size: 0.85rem;'>Dev & Designer</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Contexto Dinâmico (PDF ou Wiki)
        st.subheader("Anexe um PDF")
        pdf_file = st.file_uploader("Anexe um PDF", type="pdf", label_visibility="collapsed")
        
        if pdf_file:
            st.info(f"📄 {pdf_file.name}")
            retriever = process_pdf_func(pdf_file)
        else:
            st.caption("Modo: Wikipedia Local")
            retriever = init_wiki_func()

        st.markdown("---")
        if st.button("➕ Nova conversa"):
            st.session_state.chat_history = []
            st.session_state.resposta_atual = ""
            st.session_state.gerou_agora = False
            st.rerun()

        # Histórico Recente
        st.subheader("Recentes")
        if st.session_state.historico_objetos:
            st.markdown("<div class='history-scroll'>", unsafe_allow_html=True)
            for i, obj in enumerate(reversed(st.session_state.historico_objetos)):
                label = (obj['pergunta'][:28] + '..') if len(obj['pergunta']) > 28 else obj['pergunta']
                if st.button(f"💬 {label}", key=f"h_{i}", use_container_width=True):
                    st.session_state.pergunta_atual = obj['pergunta']
                    st.session_state.resposta_atual = obj['resposta']
                    st.session_state.gerou_agora = False
                    st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
            
        return pdf_file, retriever