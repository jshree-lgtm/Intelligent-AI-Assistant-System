import streamlit as st

from modules import sentiment
from modules import medical
from modules import multilingual
from modules import vision
from modules import research 
from modules import knowledge_update


st.set_page_config(
    page_title="AI Internship Project",
    page_icon="🤖"
)

st.title("🤖 AI Internship Project")

project = st.sidebar.selectbox(
    "Select Module",
    [
        "Sentiment Analysis",
        "Medical Assistant",
        "Multilingual Chatbot",
        "Multi-Modal AI Assistant",
        "Research Assistant",
        "Knowledge Base Update"
    ]
)

if project == "Sentiment Analysis":
    sentiment.show()

elif project == "Multilingual Chatbot":
    multilingual.show()

elif project == "Medical Assistant":
    medical.show()

elif project == "Multi-Modal AI Assistant":
    vision.show()

elif project == "Research Assistant":
    research.show()

elif project == "Knowledge Base Update":
    knowledge_update.show()


st.write(f"Selected: {project}")