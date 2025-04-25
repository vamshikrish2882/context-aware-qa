# app.py

import streamlit as st
import fitz  # PyMuPDF
import os
from src.qa_llm import ask_together_ai
from src.knowledge_graph import visualize_knowledge_graph

# Set page config
st.set_page_config(page_title="Generative AI Explorer", layout="wide")

st.title(" Generative AI Consulting Report Explorer")

# --- Upload PDF ---
uploaded_file = st.file_uploader(" Upload a consulting PDF", type=["pdf"])
if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success(" PDF uploaded successfully!")

    # Extract text using PyMuPDF
    doc = fitz.open("temp.pdf")
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    st.subheader(" Extracted Text Preview")
    st.text_area("Extracted Text", full_text[:2000], height=200)

    # --- LLM QA Section ---
    st.subheader(" Ask a Question")
    question = st.text_input("Type your question about this report:")
    if question:
        with st.spinner("Generating answer..."):
            answer = ask_together_ai(question, full_text[:5000])
        st.markdown(" **Answer:**")
        st.write(answer)

    # --- Knowledge Graph Section ---
    st.subheader(" Knowledge Graph")
    st.markdown("This is a sample knowledge graph based on common themes from the report.")
    visualize_knowledge_graph([
        ("Generative AI", "has property", "Low-code"),
        ("Generative AI", "enables", "Productivity gains"),
        ("Generative AI", "poses risk", "Security issues"),
        ("Generative AI", "poses risk", "Bias"),
        ("Generative AI", "requires", "Human feedback"),
        ("Companies", "can train", "Custom LLMs"),
        ("Companies", "can fine-tune", "LLMs"),
        ("ChatGPT", "is an example of", "Generative AI"),
    ])
