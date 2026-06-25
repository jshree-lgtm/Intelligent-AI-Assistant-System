import streamlit as st
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="qwen3:8b"
)
# Embedding Model
embedder = SentenceTransformer(
    "all-MiniLM-L6-v2"
)
INDEX_PATH = "vector_db/faiss_index.bin"
METADATA_PATH = "vector_db/metadata.pkl"

def show():
    st.header("📚 Research Assistant")

    if st.button("🗑 Clear Chat"):
        st.session_state.research_chat = []
        st.rerun()

    if "research_chat" not in st.session_state:
        st.session_state.research_chat = []
    st.write(
        "Ask research questions using uploaded documents and AI knowledge."
    )
    for role, message in st.session_state.research_chat:
        with st.chat_message(role):
            st.write(message)
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    paper_search = st.text_input(
        "🔍 Search Research Papers"
    )
    if paper_search:
        try:
            with open(
                METADATA_PATH,
                "rb"
            ) as f:
                metadata = pickle.load(f)
            matches = []
            for chunk in metadata:
                if paper_search.lower() in chunk.lower():
                    matches.append(chunk)
            st.subheader(
                "📄 Matching Research Content"
            )
            if matches:
                for match in matches[:5]:
                    st.write(
                        match[:500]
                    )
            else:
                st.info(
                    "No matching research content found."
                )
        except:
            st.warning(
                "Knowledge base not available."
            )
    question = st.chat_input(
        "Ask a research question"
    )

    if question:
        st.session_state.research_chat.append(
            ("user", question)
        )

        with st.chat_message("user"):
            st.write(question)

        if question.strip() == "":
            st.warning(
                "Please enter a question."
            )
            return
        try:
            context = ""
            knowledge_used = False
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
                best_distance = float(
                    distances[0][0]
                )
                retrieved_chunks = []
                top_paper = ""
                for idx in indices[0]:
                    if (
                        idx >= 0
                        and idx < len(metadata)
                    ):
                        chunk = metadata[idx]
                        if chunk not in retrieved_chunks:
                            if top_paper == "":
                                top_paper = chunk[:300]
                            retrieved_chunks.append(
                                chunk
                            )
                st.write(f"Similarity Distance: {best_distance}")

                if best_distance < 3.0:
                    context = "\n\n".join(
                        retrieved_chunks
                    )[:4000]
                    knowledge_used = True
                else:
                    context = ""
                    knowledge_used = False
            except:
                context = ""
                knowledge_used = False
            history = "\n".join(
                [
                    f"{role}: {msg}"
                    for role, msg in st.session_state.research_chat[-6:]
                ]
            )
            if knowledge_used:
                prompt = f"""
You are an expert research assistant.
Previous Conversation:
{history}
Use the uploaded knowledge base information whenever relevant.
Knowledge Base:
{context}
Question:
{question}
If the user asks "summarize this paper", "summarize it", or "explain this paper",
assume they are referring to the retrieved Knowledge Base above and summarize it.

Instructions:
- Answer clearly and naturally.
- Keep the response concise.
- Use bullet points if helpful.
- Focus only on the user's question.
- Avoid long academic reports unless specifically requested.
"""
            else:
                prompt = f"""
You are an intelligent research assistant.
Previous Conversation:
{history}
Question:
{question}
Instructions:
- Answer clearly and naturally.
- Keep the answer between 50 and 250 words.
- Use simple language.
- Use bullet points if useful.
- Avoid unnecessary sections and headings.
- Give examples when appropriate.
"""

            with st.spinner(
                "Analyzing..."
            ):
                response = model.invoke(prompt)

            st.session_state.research_chat.append(
                ("assistant", response.content)
            )

            with st.chat_message("assistant"):
                st.write(response.content)
            if "machine learning" in question.lower():
                st.subheader(
                    "🧠 Concept Visualization"
                )
                st.write("""
Artificial Intelligence
↓
Machine Learning
↓
Deep Learning
↓
Neural Networks
""")
            elif "deep learning" in question.lower():
                st.subheader(
                    "🧠 Concept Visualization"
                )
                st.markdown("""
### Artificial Intelligence

⬇️

### Machine Learning

⬇️

### Deep Learning

⬇️

### Neural Networks
""")

            if knowledge_used:
                st.write("### 📄 Top Retrieved Research Paper")
                st.write(top_paper)
                with st.expander(
                    "🔍 View Retrieved Knowledge"
                ):
                    st.write(
                        context[:2000]
                    )
            else:
                st.info(
                    "🤖 Answer generated using general knowledge."
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