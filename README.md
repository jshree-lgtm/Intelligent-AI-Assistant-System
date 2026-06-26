# 🤖 Intelligent AI Assistant System
## 🎯 Objective

To design and develop a unified AI assistant system that integrates multiple NLP, RAG, and multimodal AI capabilities into a single interactive platform.


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

## Problem Statement

Modern AI applications are often fragmented, with separate tools for sentiment analysis, medical Q&A, multilingual chat, and research assistance.

This project aims to build a unified Intelligent AI Assistant System that integrates multiple AI capabilities into a single platform, enabling users to:
- Interact with multiple AI services in one interface
- Access domain-specific assistants (medical, research, multilingual, vision)
- Improve knowledge retrieval using vector databases and LLMs

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

## Methodology

The system follows a modular AI pipeline:

1. **User Input Layer**
   - Streamlit UI collects user queries

2. **Intent Routing**
   - Detects which AI module to activate

3. **Processing Layer**
   - Uses LLMs (Gemini / Qwen3)
   - Uses LangChain for orchestration

4. **Retrieval Layer**
   - FAISS vector database for semantic search
   - Embeddings via Sentence Transformers

5. **Specialized AI Modules**
   - NLP (sentiment, multilingual chat)
   - RAG (medical + research assistants)
   - Computer Vision (multi-modal assistant)

6. **Response Generation**
   - Context-aware output generated using LLMs

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

## Results

The system successfully demonstrates:

- Sentiment classification accuracy in customer chat scenarios
- Accurate retrieval of medical answers using MedQuAD dataset
- Effective multilingual responses across 4+ languages
- Context-aware research summarization using arXiv papers
- Improved response relevance using FAISS vector search
- Ability to process both text and image inputs in multi-modal mode

### Performance Highlights
- Fast response time using local embeddings + FAISS
- Improved contextual accuracy with RAG-based architecture
- Modular design allows independent scaling of AI components

---

## Project Screenshots

(Refer to Screenshots folder in repository)

---

##  Internship Tasks Implemented

✅ Sentiment-Aware Customer Support Chatbot

✅ Medical Q&A Chatbot using MedQuAD Dataset

✅ Dynamic Knowledge Base Expansion

✅ Research Assistant using arXiv Papers

✅ Multi-Modal AI Assistant

✅ Multilingual Conversational Chatbot

---

## 🚀 Future Improvements

- Deployment using Docker / Cloud (AWS or Azure)
- Real-time voice assistant integration
- Improved model fine-tuning for domain-specific tasks
- User authentication system

---

## Developer

Shreehaarini J

B.Tech Artificial Intelligence and Data Science

---

##  Disclaimer

This project is developed for educational and research purposes. Medical responses are informational only and should not be considered professional medical advice.
