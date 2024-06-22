import streamlit as st
from google.cloud import bigquery
import os
import pandas as pd


def show():
    st.title("Exams Page 📝")
    st.write("Here you can take various exams. (Functionality to be implemented)")

    # Crea un cliente de BigQuery
    client = bigquery.Client()

    # Define la consulta
    query = """
        SELECT *
        FROM `qwiklabs-asl-03-2bf18f19f570.oposiciones_TAI.oposiciones_TAI` 
    """

    # Ejecuta la consulta
    query_job = client.query(query)
    results = query_job.result()

    # Convierte los resultados a un DataFrame de pandas
    df = pd.DataFrame(list(results))

    # Muestra los datos en Streamlit
    st.write("## Datos de la tabla 'oposiciones_TAI'")
    st.dataframe(df)
