import streamlit as st
from google.cloud import bigquery
import pandas as pd


def show():
    st.title("Exams Page 📝")
    st.write("Here you can take various exams.")

    # Inyectar CSS personalizado para cambiar el color de los botones de radio
    st.markdown(
        """
        <style>
        div[role="radiogroup"] > label > div[role="radio"] > div:first-child {
            background-color: black !important;
        }
        div[role="radiogroup"] > label > div[role="radio"] > div:first-child > div {
            background-color: black !important;
        }
        div[role="radiogroup"] > label > div[role="radio"] > div:first-child > div > input[type="radio"]:checked + div {
            background-color: black !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


    # Crea un cliente de BigQuery
    client = bigquery.Client()

    # Define la consulta
    query = """
        SELECT question, answer_a, answer_b, answer_c, answer_d, correct_answer, theme, justification
        FROM `qwiklabs-asl-03-2bf18f19f570.oposiciones_TAI.oposiciones_TAI`
    """

    # Ejecuta la consulta
    query_job = client.query(query)
    results = query_job.result()

    # Convertir los resultados a una lista de diccionarios
    rows = [dict(row) for row in results]

    # Convertir la lista de diccionarios a un DataFrame de pandas
    df = pd.DataFrame(rows)

    # Verificar los nombres de las columnas
    st.write("Columnas del DataFrame:")
    st.write(df.columns)

    # Mostrar las primeras filas del DataFrame para ver los datos
    st.write("Primeras filas del DataFrame:")
    st.write(df.head())

    # Crear pestañas
    tab1, tab2 = st.tabs(["Preguntas Aleatorias", "Preguntas por Temática"])

    with tab1:
        st.header("Preguntas Aleatorias")
        df_random = df.sample(frac=1).reset_index(drop=True)  # Shuffle the DataFrame
        show_questions(df_random, "random")

    with tab2:
        st.header("Preguntas por Temática")
        theme = st.selectbox("Seleccione una temática:", [
            "e-learning", "criptografía", "modelo OSI", "redes",
            "accesibilidad", "Real Decreto 1112/2018 de 7 de septiembre, sobre accesibilidad de los sitios web",
            "Guía de comunicación digital de la Administración del Estado"
        ])

        if theme:
            query_theme = f"""
                SELECT question, answer_a, answer_b, answer_c, answer_d, correct_answer, theme, justification
                FROM `qwiklabs-asl-03-2bf18f19f570.oposiciones_TAI.oposiciones_TAI`
                WHERE theme = '{theme}'
            """
            query_job_theme = client.query(query_theme)
            results_theme = query_job_theme.result()
            rows_theme = [dict(row) for row in results_theme]
            df_theme = pd.DataFrame(rows_theme)

            if not df_theme.empty:
                show_questions(df_theme, "theme")
            else:
                st.write("No hay preguntas disponibles para la temática seleccionada.")


def show_questions(df, prefix):
    user_answers = {}
    for index, row in df.iterrows():
        st.write(f"**{index + 1}. {row['question']}**")
        options = {
            'a': row['answer_a'],
            'b': row['answer_b'],
            'c': row['answer_c'],
            'd': row['answer_d']
        }
        user_answers[index] = st.radio("Seleccione una opción:", list(options.keys()), key=f"{prefix}_question_{index}")

    if st.button("Submit", key=f"{prefix}_submit"):
        correct_count = 0
        for index, row in df.iterrows():
            if user_answers[index] == row['correct_answer']:
                correct_count += 1
        st.write(f"Has acertado {correct_count} de {len(df)} preguntas.")

        st.write("### Detalle de Respuestas:")
        for index, row in df.iterrows():
            st.write(f"**{index + 1}. {row['question']}**")
            st.write(f"**Tu respuesta:** {user_answers[index]}")
            st.write(f"**Respuesta correcta:** {row['correct_answer']}")
            st.write(f"**Justificación:** {row['justification']}")
            st.write("---")

