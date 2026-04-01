<p align="right">
  <a href="#br-português">🇧🇷 Ler em Português</a> | 
  <a href="#en-english">🇺🇸 Read in English</a>
</p>

<div id="en-english">
  <h1 align="center">DEVsigner's RAGlab</h1>
  <p align="center">
    <strong>The search AI for devs, designers, and "devsigners".</strong>
  </p>

  <p align="center">
  <strong>RAGlab</strong> is an advanced <strong>Retrieval-Augmented Generation (RAG)</strong> system that leverages OpenAI's reasoning capabilities via OpenRouter, Wikipedia, or dynamic documents (PDF Upload). It focuses on merging robust data processing with a refined interface for the creative ecosystem.
  </p>

  <p align="center">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" />
    <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" />
  </p>

  <br>

  <h2>⚪ RAGlab Highlights</h2>

  <ul>
  <li><strong>Contextual Hybrid Search:</strong> Smart switching between General Knowledge (Local Wikipedia) and Technical PDF Analysis via drag-and-drop.</li>
  <li><strong>Modular Architecture:</strong> Fully <strong>componentized</strong> system with strict separation between Logic (RAG), Interface, Configuration, and Styles (CSS).</li>
  <li><strong>Tactile Feedback (UX):</strong> Powered by <code>st.status</code> and <code>st.toast</code>, featuring real-time streaming and session history integrated into the sidebar.</li>
  <li><strong>Transparency & Traceability:</strong> Detailed display of consulted sources, including document excerpts and metadata after every response.</li>
  </ul>

  <br>

  <h2>⚪ System Architecture</h2>

  <h4>UI Layer (User Interface)</h4>
  <ul>
    <li><strong>Streamlit</strong> — Interface orchestration.</li>
    <li><strong>Dracula Theme</strong> — Consistent visual identity in pure CSS.</li>
  </ul>

  <h4>RAG Layer (Intelligence)</h4>
  <ul>
    <li><strong>LangChain</strong> — Orchestration framework for LLMs and Document Loaders.</li>
    <li><strong>ChromaDB</strong> — Vector database for persistence and semantic search.</li>
    <li><strong>HuggingFace Embeddings</strong> — <code>mxbai-embed-large-v1</code> model for high-precision vector representation.</li>
  </ul>

  <h4>Language Models</h4>
  <ul>
    <li><strong>GPT-4o-mini</strong> — Via OpenRouter for contextual response generation.</li>
  </ul>

  <br>

  <h2>⚪ How to Run</h2>

  <h4>1. Clone and setup environment</h4>

  ```
  git clone [https://github.com/your-user/devsigners-raglab.git](https://github.com/your-user/devsigners-raglab.git)
  cd devsigners-raglab
  python -m venv venv
  source venv/bin/activate  # Windows: venv\Scripts\activate
```

<h4>2. Environment Variables</h4>
<p>Duplicate the <code>.env.example</code> file, rename it to <code>.env</code> and insert your key:</p>

```
OPENROUTER_API_KEY=your_key_here
```
<h4>3. Install Dependencies</h4>

```
pip install streamlit langchain langchain-openai chromadb sentence-transformers pypdf langchain-text-splitters python-dotenv
```


<h4>4. Run the Lab</h4>

```
streamlit run interface_rag.py
```
</div>

<hr>
<br>

<div id="br-português">
<h1 align="center">DEVsigner's RAGlab</h1>
<p align="center">
  <strong>A IA de busca dos devs, designers e "devsigners".</strong>
</p>

<p align="center">
O <strong>RAGlab</strong> é um sistema avançado de <strong>Retrieval-Augmented Generation (RAG)</strong> que utiliza as capacidades de raciocínio da OpenAI via OpenRouter, Wikipedia ou documentos dinâmicos (Upload de PDF). O foco é unir a robustez do processamento de dados com uma interface refinada para o ecossistema criativo.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" />
</p>

<br>

<h2>⚪ Diferenciais do RAGlab</h2>

<ul>
<li><strong>Busca Híbrida Contextual:</strong> Alternância inteligente entre consulta de Conhecimento Geral (Wikipedia Local) e Análise de PDFs Técnicos via drag-and-drop.</li>
<li><strong>Arquitetura Modular:</strong> Sistema totalmente <strong>componentizado</strong> com separação rigorosa entre Lógica (RAG), Interface, Configurações e Estilos (CSS).</li>
<li><strong>Feedback Tátil (UX):</strong> Uso de <code>st.status</code> e <code>st.toast</code>, além de Streaming em tempo real e Histórico de Sessão integrado à barra lateral.</li>
<li><strong>Transparência & Rastreabilidade:</strong> Exibição detalhada das fontes consultadas, incluindo trechos do documento e metadados após cada resposta.</li>
</ul>

<br>

<h2>⚪ Arquitetura do Sistema</h2>

<h4>Camada de UI (User Interface)</h4>
<ul>
  <li><strong>Streamlit</strong> — Orquestração da interface.</li>
  <li><strong>Dracula Theme</strong> — Identidade visual consistente em CSS puro.</li>
</ul>

<h4>Camada de RAG (Inteligência)</h4>
<ul>
  <li><strong>LangChain</strong> — Framework de orquestração de LLMs e Document Loaders.</li>
  <li><strong>ChromaDB</strong> — Banco de dados vetorial para persistência e busca semântica.</li>
  <li><strong>HuggingFace Embeddings</strong> — Modelo <code>mxbai-embed-large-v1</code> para representação vetorial de alta precisão.</li>
</ul>

<h4>Modelos de Linguagem</h4>
<ul>
  <li><strong>GPT-4o-mini</strong> — Via OpenRouter para geração de respostas contextuais.</li>
</ul>

<br>

<h2>⚪ Como Executar</h2>

<h4>1. Clone e configure o ambiente</h4>

```
git clone https://github.com/seu-usuario/devsigners-raglab.git
cd devsigners-raglab
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

<h4>2. Variáveis de Ambiente</h4>
<p>Duplique o arquivo <code>.env.example</code>, renomeie para <code>.env</code> e insira sua chave:</p>

```
OPENROUTER_API_KEY=sua_chave_aqui
```

<h4>3. Instale as dependências</h4>

```
pip install streamlit langchain langchain-openai chromadb sentence-transformers pypdf langchain-text-splitters python-dotenv
```
<h4>4. Execute o Lab</h4>

```
streamlit run interface_rag.py
```
<h2>⚪ Estrutura do Projeto</h2>

```
├── interface_rag.py   # Ponto de entrada (Main)
├── rag_engine.py      # Processamento e LLM
├── sidebar.py         # Componente visual da barra lateral
├── config.py          # Configurações e utilitários
├── style.css          # Design System
├── chroma_db/         # Banco vetorial (Local)
└── .env.example       # Template de credenciais
```

<h2>👩‍💻 Developed by/ Desenvolvido por:</h2>

<p>
<strong>Giselle Garcia</strong>
</p>
<p>
Full-Stack Developer & UX/UI Designer
</p>
<p>
  2026
</p>
