import streamlit as st
import google.generativeai as genai
import pandas as pd
import re
from config import API_KEY


genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def show():

    if "sentiment_history" not in st.session_state:
        st.session_state.sentiment_history = []

    if "emotion_df" not in st.session_state:
        st.session_state.emotion_df = pd.DataFrame()

    st.header("😊 Emotion-Aware Sentiment Analysis Chatbot")

    st.write(
        "Analyze customer emotions and generate appropriate responses."
    )

    if st.button("🗑 Clear Chat"):

        st.session_state.sentiment_history = []
        st.session_state.emotion_df = pd.DataFrame()

        st.rerun()

    if st.session_state.sentiment_history:

        st.subheader("💬 Conversation History")

        for msg in st.session_state.sentiment_history:
            st.write(msg)

        if ("emotion_df" in st.session_state and st.session_state.emotion_df is not None):

            st.subheader("📊 Emotion Distribution")

            st.bar_chart(
                st.session_state.emotion_df.set_index("Emotion")
            )

    user_message = st.chat_input(
        "Type customer message..."
    )

    if user_message:

        if not user_message.strip():
            st.warning("Please enter a message.")
            return
        
        history = "\n".join(
            st.session_state.sentiment_history[-6:]
        )   

        prompt = f"""
        You are an expert customer sentiment analyst.
        Previous Conversation:
        {history}

        Analyze the following customer message.

        Return the result in EXACTLY this format:

Sentiment:
Choose exactly ONE of these values:
Positive
Negative
Neutral

Primary Emotion:
<emotion>

Emotion Breakdown:
<emotion> - <percentage>%
<emotion> - <percentage>%
<emotion> - <percentage>%

Customer Satisfaction Risk:
Low / Medium / High

Explanation:
<short explanation>

Suggested Response:
<professional customer service response>

        Use only emotions from:
        Happy, Excited, Relieved, Satisfied,
        Neutral, Confused, Concerned,
        Sad, Frustrated, Angry, Disappointed

        Percentages must add up to 100.

        Customer Message:
        {user_message}
        """

        with st.spinner("Analyzing emotions..."):

            try:
                response = model.generate_content(prompt)
                response_text = response.text
            except Exception as e:
                st.error(f"Error generating response: {e}")
                return

            emotion_matches = re.findall(
                r'([A-Za-z]+)\s*-\s*(\d+(?:\.\d+)?)%',
                response_text
            )
            if emotion_matches:

                emotions = []
                percentages = []

                for emotion, percent in emotion_matches:

                    emotions.append(emotion)
                    percentages.append(int(percent))

                emotion_data = {
                    "Emotion": emotions,
                    "Percentage": percentages
                }

                df = pd.DataFrame(emotion_data)

                st.session_state.emotion_df = df

            st.session_state.sentiment_history.append(
                f"🧑 Customer: {user_message}"
            )

            st.session_state.sentiment_history.append(
                f"🤖 Bot: {response_text}"
            )
                        
            st.rerun()