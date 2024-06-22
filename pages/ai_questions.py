import os
import streamlit as st
import vertexai
from vertexai.generative_models import (
    GenerationConfig,
    GenerativeModel,
    HarmBlockThreshold,
    HarmCategory,
)

# Configuración del proyecto de Google Cloud
PROJECT_ID = os.environ.get("GCP_PROJECT")  # Your Google Cloud Project ID
LOCATION = os.environ.get("GCP_REGION")  # Your Google Cloud Project Region
vertexai.init(project=PROJECT_ID, location=LOCATION)

@st.cache_resource
def load_models():
    """
       Load the generative models for text and multimodal generation.

       Returns:
           Tuple: A tuple containing the text model and multimodal model.
       """
    text_model_pro = GenerativeModel("gemini-1.0-pro")
    multimodal_model_pro = GenerativeModel("gemini-1.0-pro-vision")
    return text_model_pro, multimodal_model_pro

def get_gemini_pro_text_response(
    model: GenerativeModel,
    prompt: str,
    generation_config: GenerationConfig,
    stream: bool = True,
):
    safety_settings = {
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    }

    responses = model.generate_content(
        prompt,
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=stream,
    )

    final_response = []
    for response in responses:
        try:
            final_response.append(response.text)
        except IndexError:
            final_response.append("")
            continue
    return " ".join(final_response)

def show():
    st.title("AI Generated Questions 🤖")
    text_model_pro, multimodal_model_pro = load_models()
    st.subheader("Generate questions based on a theme")

    # Input for the theme
    theme = st.text_input("Enter the theme:", key="theme", value="Networks")
    creativity_level = st.radio(
        "Select the creativity level:",
        ["Low", "High"],
        key="creativity_level",
        horizontal=True,
    )

    if creativity_level == "Low":
        config = GenerationConfig(
            temperature=0.30,
            max_output_tokens=2048,
        )
    else:
        config = GenerationConfig(
            temperature=0.8,
            max_output_tokens=2048,
        )

    prompt = f"""Write 20 questions on the following theme: \n
        Theme: {theme} \n
        Below each question, provide four possible answers with only one correct answer.
        Below, provide the correct answer.
        Below, provide a reasoned justification for why it is valid. If you have a reference source, it is better. Do not invent anything; if you do not know the justification, indicate it.
        show me everything in Spanish
        """

    generate_questions = st.button("Generate Questions", key="generate_questions")
    if generate_questions and prompt:
        with st.spinner("Generating your questions using Gemini 1.0 Pro ..."):
            tab_questions, tab_prompt = st.tabs(["Questions", "Prompt"])
            with tab_questions:
                response = get_gemini_pro_text_response(
                    text_model_pro,
                    prompt,
                    generation_config=config,
                )
                if response:
                    st.write("Generated Questions:")
                    st.write(response)
            with tab_prompt:
                st.text(prompt)
