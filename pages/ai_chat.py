import streamlit as st


def generate_response(prompt):
    openai.api_key = 'YOUR_OPENAI_API_KEY'
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()


def show():
    st.title("AI Chat 🗣️")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    user_input = st.text_input("You: ")
    if st.button("Send"):
        st.session_state.messages.append(f"You: {user_input}")
        ai_response = generate_response(user_input)
        st.session_state.messages.append(f"AI: {ai_response}")

    for message in st.session_state.messages:
        st.write(message)
