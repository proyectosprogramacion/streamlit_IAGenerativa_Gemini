import streamlit as st

def generate_question():
    return "ai_questions"

def show():
    st.title("AI Generated Questions 🤖")
    prompt = st.text_input("Enter a topic or question prompt:")
    if st.button("Generate Question"):
        ai_question = generate_question(prompt)
        st.write("Generated Question:")
        st.write(ai_question)
