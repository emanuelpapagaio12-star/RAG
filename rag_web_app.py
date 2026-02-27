import streamlit as st
import os
import secrets
from rag_system import RAGSystem

# --- Configuración de la Página ---
st.set_page_config(
    page_title="RAG Intelligence - Chat with PDF",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Estilos Personalizados (Aesthetics) ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stChatFloatingInputContainer {
        bottom: 20px;
    }
    .stChatMessage {
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 10px;
        border: 1px solid #30363d;
    }
    .user-message {
        background-color: #161b22;
    }
    .assistant-message {
        background-color: #21262d;
        border-left: 5px solid #238636;
    }
    .title-container {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 2rem;
        background: linear-gradient(90deg, #1f4037 0%, #99f2c8 100%);
        border-radius: 15px;
        color: white;
        margin-bottom: 2rem;
    }
    .sidebar .sidebar-content {
        background-color: #161b22;
    }
    h1, h2, h3 {
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Inicialización de Estado ---
if "rag_instance" not in st.session_state:
    st.session_state.rag_instance = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "processed_file" not in st.session_state:
    st.session_state.processed_file = None

# --- Cabecera ---
st.markdown("""
    <div class="title-container">
        <h1>🧠 RAG Intelligence System</h1>
    </div>
    """, unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/337/337946.png", width=100)
    st.header("Document Center")
    st.info("Sube tu archivo PDF para comenzar la extracción de conocimiento.")
    
    uploaded_file = st.file_uploader("Arrastra tu PDF aquí", type="pdf")
    
    if uploaded_file:
        if st.session_state.processed_file != uploaded_file.name:
            if st.button("🚀 Procesar e Indexar"):
                with st.spinner("Analizando documento y creando base vectorial..."):
                    # Asegurar directorio temporal
                    temp_path = "uploads"
                    if not os.path.exists(temp_path):
                        os.makedirs(temp_path)
                    
                    full_path = os.path.join(temp_path, uploaded_file.name)
                    with open(full_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    
                    # Inicializar RAG
                    try:
                        rag = RAGSystem(full_path)
                        rag.ingest()
                        st.session_state.rag_instance = rag
                        st.session_state.processed_file = uploaded_file.name
                        st.success(f"¡{uploaded_file.name} listo para preguntas!")
                    except Exception as e:
                        st.error(f"Error al procesar: {e}")

    if st.session_state.rag_instance:
        st.divider()
        st.success(f"Activo: {st.session_state.processed_file}")
        if st.button("Clear Chat"):
            st.session_state.chat_history = []
            st.rerun()

# --- Main Interface ---
if not st.session_state.rag_instance:
    st.warning("⚠️ Esperando documento... Por favor, sube un PDF en la barra lateral.")
    
    # Showcase features
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🔍 Búsqueda Semántica")
        st.write("Encuentra el contexto exacto sin necesidad de palabras clave perfectas.")
    with col2:
        st.markdown("### ⚡ FAISS Indexing")
        st.write("Búsqueda ultrarrápida incluso en documentos extensos.")
    with col3:
        st.markdown("### 📄 Local Processing")
        st.write("Tus datos se procesan localmente para mayor privacidad.")
else:
    # Mostrar historial de chat
    for chat in st.session_state.chat_history:
        with st.chat_message(chat["role"]):
            st.markdown(chat["content"])

    # Input de chat
    if prompt := st.chat_input("Escribe tu pregunta sobre el documento..."):
        # Agregar mensaje de usuario
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generar respuesta
        with st.chat_message("assistant"):
            with st.spinner("Consultando base de conocimientos..."):
                try:
                    results = st.session_state.rag_instance.query(prompt)
                    
                    if not results:
                        response = "No he encontrado información específica sobre eso en el documento."
                    else:
                        # Formatear respuesta con los fragmentos encontrados
                        response = "He encontrado los siguientes pasajes relevantes en el documento:\n\n"
                        for i, doc in enumerate(results):
                            page_num = doc.metadata.get('page', 'N/A')
                            response += f"**Pasaje {i+1} (Página {page_num}):**\n"
                            response += f"_{doc.page_content.strip()}_\n\n"
                        
                        response += "---"
                    
                    st.markdown(response)
                    st.session_state.chat_history.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(f"Ocurrió un error al consultar: {e}")

st.markdown("---")
st.caption("Desarrollado con Streamlit, LangChain y FAISS")
