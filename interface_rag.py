import streamlit as st
from config import load_css
from sidebar import render_sidebar
from rag_engine import process_pdf, init_wiki_rag, get_llm
from langchain_core.messages import HumanMessage, AIMessage

# 1. SETUP
st.set_page_config(page_title="DEVsigner RAGlab", page_icon="👩‍💻", layout="centered")
load_css("style.css")

# 2. GESTÃO DE ESTADO
for key in ["chat_history", "historico_objetos"]:
    if key not in st.session_state: st.session_state[key] = []
if "pergunta_atual" not in st.session_state: st.session_state.pergunta_atual = ""
if "resposta_atual" not in st.session_state: st.session_state.resposta_atual = ""
if "gerou_agora" not in st.session_state: st.session_state.gerou_agora = False

# 3. SIDEBAR COMPONENTIZADA
pdf_file, current_retriever = render_sidebar(process_pdf, init_wiki_rag)

# 4. ÁREA PRINCIPAL
st.markdown("<h1 style='text-align: center; color: #bd93f9; margin-bottom: 0px;'>RAGlab</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #44475a; font-style: thin; font-size: 1.1rem; margin-top: 0px;'>A IA de busca dos devs, designers, devsigners e simpatizantes.</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

if st.session_state.resposta_atual:
    with st.chat_message("user"): st.write(st.session_state.pergunta_atual)
    with st.chat_message("assistant"):
        if not st.session_state.gerou_agora: st.markdown(st.session_state.resposta_atual)

pergunta = st.chat_input("O que deseja explorar hoje?")

if pergunta:
    llm = get_llm()

    label_busca = "📚 Lendo seu PDF..." if pdf_file else "🌐 Consultando Wikipedia..."
    with st.status(label_busca, expanded=False) as status:
        docs = current_retriever.invoke(pergunta)
        contexto = "\n\n".join([d.page_content for d in docs])
        status.update(label="✅ Conhecimento processado!", state="complete")
        st.toast(f"Encontrei {len(docs)} trechos relevantes!", icon="🔍")

    st.session_state.chat_history.append(HumanMessage(content=f"Contexto: {contexto}\n\nPergunta: {pergunta}"))
    with st.chat_message("user"): st.write(pergunta)
    
    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        for chunk in llm.stream(st.session_state.chat_history):
            full_response += (chunk.content or "")
            placeholder.markdown(full_response + "▌")
        placeholder.markdown(full_response)

    if docs:
        with st.expander("📚 Fontes consultadas"):
            for i, d in enumerate(docs):
                origem = d.metadata.get('title', d.metadata.get('source', 'Documento Local'))
                st.markdown(f"**{i+1}. {origem}**\n\n_{d.page_content[:300]}..._")

    st.session_state.chat_history.append(AIMessage(content=full_response))
    if not any(item['pergunta'] == pergunta for item in st.session_state.historico_objetos):
        st.session_state.historico_objetos.append({"pergunta": pergunta, "resposta": full_response})
    st.session_state.resposta_atual, st.session_state.pergunta_atual, st.session_state.gerou_agora = full_response, pergunta, True