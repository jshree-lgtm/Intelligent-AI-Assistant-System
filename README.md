# 🤖 Intelligent AI Assistant System

## 📌 Overview

The Intelligent AI Assistant System is a Streamlit-based AI application developed as part of an AI & Data Science Internship.

The project integrates multiple AI capabilities into a single platform, including:

* Sentiment Analysis Chatbot
* Medical Question Answering Assistant
* Multilingual Conversational AI
* Multi-Modal Vision Assistant
* Research Assistant
* Dynamic Knowledge Base Expansion

The system demonstrates Natural Language Processing (NLP), Retrieval-Augmented Generation (RAG), Vector Databases, Computer Vision, Multilingual AI, and Large Language Model (LLM) integration.

---

## Features

### Sentiment Analysis Chatbot

* Detects customer sentiment (Positive, Negative, Neutral)
* Identifies primary emotions
* Generates professional responses
* Displays emotion distribution charts

### Medical Q&A Chatbot

* Uses MedQuAD medical dataset
* FAISS-based retrieval system
* Medical entity recognition
* Educational healthcare assistance

### Multilingual Chatbot

* Supports English, Tamil, Hindi, and Malayalam
* Handles mixed-language conversations
* Preserves context across language switches
* Uses open-source LLMs through Ollama

### Multi-Modal AI Assistant

* Understands images and text together
* Extracts visual evidence
* Performs contextual reasoning
* Provides confidence-based responses

### Research Assistant

* Uses arXiv research papers
* Research paper search
* Summarization and explanation
* Concept visualization support
* Follow-up question handling

### Knowledge Base Update System

* Upload TXT, PDF, DOCX, and PPTX files
* Automatically generates embeddings
* Updates FAISS vector database
* Expands chatbot knowledge dynamically

---

## Technologies Used

### Frontend

* Streamlit

### LLMs

* Gemini 2.5 Flash
* Qwen3:8B (Ollama)

### NLP & Retrieval

* LangChain
* Sentence Transformers
* FAISS

### Data Processing

* NumPy
* Pandas

### Document Processing

* PyPDF
* python-docx
* python-pptx

### Computer Vision

* PIL (Pillow)
* Gemini Vision

---

##  Datasets

### MedQuAD Dataset

Used for the Medical Question Answering Chatbot.

Source:
https://github.com/abachaa/MedQuAD

### arXiv Dataset

Used for the Research Assistant module.

Source:
https://www.kaggle.com/datasets/Cornell-University/arxiv

---

##  System Architecture

User Input
↓
Streamlit Interface
↓
Module Selection
↓
AI Processing Layer
↓
FAISS / LLM / Vision Models
↓
Response Generation
↓
Output to User

---

##  Installation

Clone the repository:

git clone https://github.com/jshree-lgtm/Intelligent-AI-Assistant-System.git

Navigate to project folder:

cd Intelligent-AI-Assistant-System

Install dependencies:

pip install -r requirements.txt

Run Streamlit:

streamlit run app.py

---

##  Internship Tasks Implemented

✅ Sentiment-Aware Customer Support Chatbot

✅ Medical Q&A Chatbot using MedQuAD Dataset

✅ Dynamic Knowledge Base Expansion

✅ Research Assistant using arXiv Papers

✅ Multi-Modal AI Assistant

✅ Multilingual Conversational Chatbot

---

## Developer

Shreehaarini J

B.Tech Artificial Intelligence and Data Science

---

##  Disclaimer

This project is developed for educational and research purposes. Medical responses are informational only and should not be considered professional medical advice.
