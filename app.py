import streamlit as st
import pages.home as home
import pages.questions as questions
import pages.exams as exams
import pages.ai_questions as ai_questions
import pages.ai_chat as ai_chat

# Configuración de la página
st.set_page_config(page_title="Oposiciones App", layout="wide")

# Estilos CSS para el diseño tech y juvenil
st.markdown(
    """
    <style>
    .main-header { background-color: #0f4c75; color: white; padding: 10px; text-align: center; font-size: 24px; }
    .sidebar .sidebar-content { background-color: #3282b8; color: white; }
    .nav-buttons {
        display: flex;
        justify-content: space-between;
        margin-bottom: 20px;
        width: 100%;
    }
    .nav-buttons > div {
        flex: 1;
        text-align: center;
    }
    .stButton > button {
        background-color: #1b262c;
        color: white;
        border: 1px solid #3282b8;
        padding: 10px;
        border-radius: 10px;
        cursor: pointer;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #3282b8;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Panel lateral con imagen y enlaces externos
with st.sidebar:
    st.image("resources/logo.webp", use_column_width=True)
    st.markdown("[Cuerpo de Técnicos Auxiliares de Informática de la Administración del Estado](https://sede.inap.gob.es/tai)")
    st.markdown("[Servicios informáticos UCM](https://www.ucm.es/procesos-finalizados-1)")
    st.markdown("[Programador UVA](https://pas.uva.es/1.convocatorias/index.html)")

# Menú superior
st.markdown('<div class="main-header">Tech App 💻</div>', unsafe_allow_html=True)

pages = {
    "🏠 Home": home.show,
    "❓ Questions": questions.show,
    "📝 Exams": exams.show,
    "🤖 AI Questions": ai_questions.show,
    "🗣️ AI Chat": ai_chat.show
}

# Crear un contenedor para los botones de navegación
st.markdown('<div class="nav-buttons">', unsafe_allow_html=True)
button_columns = st.columns(len(pages))

for i, page_name in enumerate(pages.keys()):
    if button_columns[i].button(page_name):
        st.session_state.page = page_name

st.markdown('</div>', unsafe_allow_html=True)

# Manejar la navegación
if 'page' not in st.session_state:
    st.session_state.page = "🏠 Home"

pages[st.session_state.page]()