import streamlit as st

def load_questions(file_path):
    with open(file_path, "r") as file:
        questions = file.readlines()
    return questions

def show():
    st.title("Questions Page 📄")
    questions = load_questions("resources/questions.txt")
    for q in questions:
        st.write(q)
