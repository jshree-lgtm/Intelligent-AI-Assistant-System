import streamlit as st
from PIL import Image
import google.generativeai as genai
from config import API_KEY

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def show():

    if "vision_history" not in st.session_state:
     st.session_state.vision_history = []

    st.header("🤖 Multi-Modal AI Assistant")
    if st.button("🗑 Clear Conversation"):

        st.session_state.vision_history = []

        st.rerun()

    st.write(
        "Upload an image and ask questions about it. The assistant will reason using both image and text."
    )

    uploaded_file = st.file_uploader(
        "Choose an image",
        type=["jpg", "jpeg", "png"]
    )

    user_question = st.chat_input(
    "Ask a question about the image..."
)

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )
        if st.session_state.vision_history:

            st.subheader("💬 Conversation History")

            for msg in st.session_state.vision_history:

                st.write(msg)

        if user_question:

            if uploaded_file is None:
                st.warning("Please upload an image first.")
                return

            if not user_question.strip():

                st.warning("Please enter a question.")
                return

            history = "\n".join(
                 st.session_state.vision_history[-6:]
            )

            with st.spinner("Analyzing image and reasoning..."):

                try:
                    analysis_prompt = """
Analyze this image and provide:

Objects Detected:
Text Detected:
Scene Description:
Important Visual Evidence:
Confidence Level: High/Medium/Low

Only use visible information.
"""
                    prompt = f"""
You are a Multi-Modal AI Assistant.

Previous Conversation:
{history}

User Question:
{user_question}

Using ONLY the visual evidence above:

Return:

Answer:
...

Confidence:
High/Medium/Low

Validation:
Explain why the answer is supported by the visual evidence.

If evidence is insufficient, clearly say so.
"""
                    response = model.generate_content(
                        [prompt, image]
                    )
                    st.session_state.vision_history.append(
                        f"🧑 User: {user_question}"
                    )

                    st.session_state.vision_history.append(
                        f"🤖 Assistant: {response.text}"
                    )
                    st.subheader("🤖 Assistant Response")
                    st.write(response.text)
                    st.rerun()

                except Exception as e:

                    if "429" in str(e):

                        st.warning(
                            "⚠️ Gemini quota exceeded. Please wait a minute and try again."
                        )

                    else:

                        st.error(f"Error: {e}")