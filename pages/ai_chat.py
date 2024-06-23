import streamlit as st
import streamlit.components.v1 as components

# Función principal para mostrar la pestaña de AI Chat
def show():
    st.title("AI Chat 🗣️")

    # Definir las subpestañas
    st.markdown("""
        <style>
        .sub-tabs {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
            width: 100%;
        }
        .sub-tabs > div {
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
    """, unsafe_allow_html=True)

    sub_tabs = ["💻 Chat TAI", "🎓 Chat UCM", "📚 Chat UVA"]
    sub_tab_buttons = st.columns(len(sub_tabs))

    if "sub_tab" not in st.session_state:
        st.session_state.sub_tab = "💻 Chat TAI"

    for i, sub_tab in enumerate(sub_tabs):
        if sub_tab_buttons[i].button(sub_tab):
            st.session_state.sub_tab = sub_tab

    st.markdown('<hr>', unsafe_allow_html=True)

    if st.session_state.sub_tab == "💻 Chat TAI":
        st.header("💻 Cuerpo de Técnicos Auxiliares de Informática de la Administración del Estado")
        show_chat_and_links(handle_chat_tai)

    elif st.session_state.sub_tab == "🎓 Chat UCM":
        st.header("🎓 Chat UCM")
        show_chat_and_links(handle_chat)

    elif st.session_state.sub_tab == "📚 Chat UVA":
        st.header("📚 Chat UVA")
        show_chat_and_links(handle_chat)


def show_chat_and_links(chat_function):
    col1, col2 = st.columns([2, 1])  # Ajusta el ancho de las columnas según sea necesario

    with col1:
        st.subheader("Chat 🗨️")
        chat_function()

    with col2:
        st.subheader("Enlaces 🔗")
        st.markdown("""
        <style>
        .resource-button {
            background-color: #1b262c;
            color: white;
            border: 1px solid #3282b8;
            padding: 10px;
            border-radius: 10px;
            cursor: pointer;
            text-align: center;
            margin-bottom: 10px;
            display: block;
            text-decoration: none;
        }
        .resource-button:hover {
            background-color: #3282b8;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown('<a class="resource-button" href="https://drive.google.com/drive/folders/1vFizYkFUViPU8MCWNrkAGPeBjlPxp-Ev" target="_blank">📜 Acceder a las Leyes del Cuerpo de Técnicos Auxiliares de Informática de la Administración del Estado (Libre)</a>', unsafe_allow_html=True)
        st.markdown('<a class="resource-button" href="https://drive.google.com/drive/folders/1imLJoez96ejYQSgPM_FXc-llTnTzRi_I" target="_blank">📘 Acceder al temario del Cuerpo de Técnicos Auxiliares de Informática de la Administración del Estado (Libre)</a>', unsafe_allow_html=True)
        st.markdown('<a class="resource-button" href="https://sites.google.com/view/cuerpotecnicosauxiliaresdeinf/" target="_blank">🔍 Acceder al buscador de consulta de las leyes</a>', unsafe_allow_html=True)


# Función para manejar el chat de Dialogflow TAI
def handle_chat_tai():
    # Insertar código HTML y JavaScript de Dialogflow y el widget de búsqueda
    components.html(
        """
        <!-- Dialogflow Widget -->
        <link rel="stylesheet" href="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/themes/df-messenger-default.css">
        <script src="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/df-messenger.js"></script>
        <df-messenger
            project-id="qwiklabs-asl-03-2bf18f19f570"
            agent-id="66c8500c-e643-4bef-a031-c26b9c93e0b7"
            language-code="es"
            max-query-length="-1">
            <df-messenger-chat chat-title=""></df-messenger-chat>
        </df-messenger>
        <style>
            df-messenger {
                z-index: 999;
                position: fixed;
                --df-messenger-font-color: #000;
                --df-messenger-font-family: Google Sans;
                --df-messenger-chat-background: #f3f6fc;
                --df-messenger-message-user-background: #d3e3fd;
                --df-messenger-message-bot-background: #fff;
                bottom: 0;
                right: 0;
                top: 0;
                width: 100%;
                height: 600px; /* Altura ajustada */
            }
        </style>

        """,
        height=600,
    )

# Función para manejar la lógica del chat
def handle_chat():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    user_input = st.text_input("You: ")
    if st.button("Send"):
        st.session_state.messages.append(f"You: {user_input}")

    for message in st.session_state.messages:
        st.write(message)
