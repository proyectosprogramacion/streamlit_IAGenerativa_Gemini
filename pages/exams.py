import streamlit as st
from google.cloud import bigquery
import pandas as pd


def show():
    st.title("Exams Page 📝")
    st.write("Here you can take various exams.")



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

    # Mostrar las preguntas y opciones de respuesta
    st.write("## Examen")
    user_answers = {}
    for index, row in df.iterrows():
        st.write(f"**{index + 1}. {row['question']}**")
        options = {
            'a': row['answer_a'],
            'b': row['answer_b'],
            'c': row['answer_c'],
            'd': row['answer_d']
        }
        user_answers[index] = st.radio("Seleccione una opción:", list(options.keys()), key=f"question_{index}")

    if st.button("Submit"):
        correct_count = 0
        for index, row in df.iterrows():
            if user_answers[index] == row['correct_answer']:
                correct_count += 1
        st.write(f"Has acertado {correct_count} de {len(df)} preguntas.")


if __name__ == "__main__":
    show()

