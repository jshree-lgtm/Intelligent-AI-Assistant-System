import streamlit as st
import google.generativeai as genai
import faiss
import pickle
import numpy as np

from sentence_transformers import SentenceTransformer
from config import API_KEY

# Gemini Setup
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# Embedding Model
embedder = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

INDEX_PATH = "medical_db/medical_index.bin"
METADATA_PATH = "medical_db/medical_metadata.pkl"

def show():

    st.header("🩺 Medical Q&A Chatbot")
    
    if st.button("🗑 Clear Chat"):
        st.session_state.medical_chat = []
        st.rerun()

    if "medical_chat" not in st.session_state:
        st.session_state.medical_chat = []
        
    st.warning(
        "This chatbot provides educational medical information only. "
        "Always consult a healthcare professional for diagnosis and treatment."
    )

    for role, message in st.session_state.medical_chat:
        with st.chat_message(role):
            st.write(message)
            
    question = st.chat_input("Ask a medical question")

    if question:

        st.session_state.medical_chat.append(
            ("user", question)
        )

        with st.chat_message("user"):
            st.write(question)

        try:

            index = faiss.read_index(
                INDEX_PATH
            )

            with open(
                METADATA_PATH,
                "rb"
            ) as f:

                metadata = pickle.load(f)

            query_embedding = embedder.encode(
                [question]
            )

            query_embedding = np.array(
                query_embedding,
                dtype="float32"
            )

            distances, indices = index.search(
                query_embedding,
                k=3
            )

            retrieved_answers = []

            for idx in indices[0]:

                if (
                    idx >= 0
                    and idx < len(metadata)
                ):

                    retrieved_answers.append(
                        metadata[idx]["answer"]
                    )

            context = "\n\n".join(
                retrieved_answers
            )
            history = "\n".join(
                [
                    f"{role}: {msg}"
                    for role, msg in st.session_state.medical_chat[-6:]
                ]
            )
            prompt = f"""
You are a medical question answering assistant.

Use the retrieved MedQuAD information whenever relevant.

If the retrieved information is incomplete,
use your own medical knowledge to provide
a complete and accurate answer.

Retrieved Medical Information:
{context}

Conversation History:
{history}

Current User Question:
{question}

Tasks:

1. Give a direct answer.
2. Explain clearly in simple language.
3. Identify symptoms if mentioned.
4. Identify diseases if mentioned.
5. Identify treatments if mentioned.

Keep the answer concise and useful.

Format:

Medical Answer:
...

Detected Symptoms:
...

Detected Diseases:
...

Detected Treatments:
...

Important Note:
This information is educational and not a medical diagnosis.
"""

            with st.spinner(
                "Analyzing..."
            ):

                response = model.generate_content(
                    prompt
                )

            st.session_state.medical_chat.append(
                ("assistant", response.text)
            )

            with st.chat_message("assistant"):
                st.write(response.text)

            with st.expander(
                "🔍 Retrieved Medical Knowledge"
            ):

                st.write(
                    context[:3000]
                )

        except Exception as e:

            if "429" in str(e):

                st.warning(
                    "⚠️ Gemini quota exceeded. Please wait a minute and try again."
                )

            else:

                st.error(
                    f"Error: {e}"
                )