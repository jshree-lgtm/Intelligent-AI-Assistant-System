import streamlit as st
from langchain_ollama import ChatOllama
from langdetect import detect

model = ChatOllama(
    model="qwen3:8b"
)

def show():

    st.header("🌍 Multilingual Chatbot")

    if "multi_history" not in st.session_state:
        st.session_state.multi_history = []

    # Display conversation
    for msg in st.session_state.multi_history:
        if msg["role"] == "user":
            with st.chat_message("user"):
                st.write(msg["content"])
        else:
            with st.chat_message("assistant"):
                st.write(msg["content"])

    if st.button("🗑 Clear Conversation"):
        st.session_state.multi_history = []
        st.rerun()

    st.write(
        "Supports multilingual conversations in English, Tamil, Hindi, and Malayalam while preserving context across language switches."
    )

    user_message = st.chat_input("Type your message...")

    if user_message:
        try:
            detected_lang = detect(user_message)
        except:
            detected_lang = "en"
        
        if not user_message.strip():
            st.warning("Please enter a message.")
            return

        # Use only recent history
        history = ""
        for item in st.session_state.multi_history[-8:]:
            history += f"{item['role']}: {item['content']}\n"

        last_answer = st.session_state.get(
            "last_answer",
            ""
        )
        prompt = f"""
You are an intelligent multilingual chatbot.
Most Recent Assistant Response:
{last_answer}
Previous Conversation:
{history}
The language detector identified the latest user message as:
{detected_lang}
Use this only as a hint. If the detected language appears incorrect, rely on the actual user message instead.
Important Context Rule:

If the user says:
- explain this
- explain it
- translate this
- translate it
- explain in Tamil
- explain in Hindi
- explain in Malayalam
- explain in English

then assume "this" refers to the MOST RECENT assistant response in the conversation history.

Do not ask what the user means unless no previous assistant response exists.
Tasks:
1. Detect the language(s) used by the user.
2. Detect whether the message is code-mixed.
3. Identify the style:
   - English
   - Tamil
   - Hindi
   - Malayalam
   - Tanglish
   - Hinglish
   - Manglish
   - Other

4. Understand the user's intent.
5. Reply naturally in the SAME language/style used by the user.

Return the answer in this format:

Detected Language:
<language>

Detected Style:
<style>

Response:
<your response>

User Message:
{user_message}
"""

        with st.spinner("Generating response..."):
            try:
                response = model.invoke(prompt)

                answer = response.content.strip()
                st.session_state.last_answer = answer
                st.session_state.multi_history.append(
                    {
                        "role": "user",
                        "content": user_message
                    }
                )

                st.session_state.multi_history.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

                st.rerun()

            except Exception as e:
                st.error(f"Error: {e}")