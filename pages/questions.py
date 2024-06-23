import streamlit as st

def load_questions(file_path):
    with open(file_path, "r", encoding="utf-8-sig") as file:
        questions = file.readlines()
    return questions

def show():
    st.title("Questions Page 📄")

    questions = load_questions("resources/questions.txt")

    st.markdown(
        """
        <style>
        .question-header {
            font-size: 24px;
            color: red; /* Red color for exam titles */
            margin-top: 20px;
            text-transform: uppercase; /* Uppercase for exam titles */
        }
        .question {
            font-size: 18px;
            color: #0f4c75; /* Dark blue color for questions */
            margin-top: 10px;
        }
        .answer {
            margin-left: 20px;
            font-size: 16px;
            color: #1b262c; /* Normal text color for answers */
        }
        .correct {
            font-weight: bold; /* Bold for correct answer */
        }
        .theme, .justification {
            font-size: 16px;
            color: #1b262c; /* Normal text color for theme and justification */
        }
        .divider {
            margin: 20px 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    for i, line in enumerate(questions):
        line = line.strip()  # Remove any leading/trailing whitespace characters
        if line.startswith("EXAMEN"):
            st.markdown(f"<div class='question-header'>{line} 📚</div>", unsafe_allow_html=True)
        elif line.startswith(tuple('1234567890')):
            st.markdown(f"<div class='question'>{line}</div>", unsafe_allow_html=True)
        elif line.startswith(('a)', 'b)', 'c)', 'd)')):
            st.markdown(f"<div class='answer'>{line}</div>", unsafe_allow_html=True)
        elif line.startswith("correcta"):
            st.markdown(f"<div class='answer correct'>{line}</div>", unsafe_allow_html=True)
        elif line.startswith("temática"):
            st.markdown(f"<div class='theme'>{line}</div>", unsafe_allow_html=True)
        elif line.startswith("justificación"):
            st.markdown(f"<div class='justification'>{line}</div>", unsafe_allow_html=True)

        # Add a horizontal line after each question block
        if (i < len(questions) - 1 and questions[i + 1].startswith(tuple('1234567890'))) or i == len(questions) - 1:
            st.markdown("<hr class='divider'>", unsafe_allow_html=True)

