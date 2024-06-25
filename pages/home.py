import streamlit as st

def show():
    st.title("Bienvenido a Mi Aplicación de Preparación de Oposiciones con IA Generativa 🌟")

    st.write("""
    Esta es una aplicación para preparar oposiciones a programador/a con IA Generativa. Nuestro objetivo es ofrecerte una experiencia de estudio moderna y eficiente, utilizando lo último en tecnología de inteligencia artificial para ayudarte a alcanzar tus metas.
    """)

    st.write("""
    El objetivo de esta aplicación es ser respetuosa con el medio ambiente y por ello el enfoque siempre es Reducir y Reutilizar el uso de la IA. Creemos que es posible utilizar tecnología avanzada de manera sostenible, minimizando el impacto ecológico.
    """)

    st.markdown("""
    Puedes leer más sobre el consumo que supone el uso de la IA en el siguiente enlace: [Consumo de IA y su Impacto Ambiental](https://earth.org/the-green-dilemma-can-ai-fulfil-its-potential-without-harming-the-environment/).
    """)

    st.write("""
    ### Uso de la Aplicación 💡
    - **Questions 📄**: Muestra preguntas de exámenes oficiales.
    - **Exams 📝**: Muestra preguntas de exámenes tanto oficiales como generadas por IA por otros usuarios. Puedes seleccionar una temática concreta.
    - **AI Questions 🤖**: Genera preguntas nuevas con IA generativa.
    - **AI Chat 🗣️**: Permite acceder a un chat con IA sobre legislación; además de recursos disponibles específicos para cada oposición.
    """)

    st.markdown(
        """
        <style>
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
