import streamlit as st
import fitz  # PyMuPDF
import os
from src.qa_llm import ask_together_ai
from src.knowledge_graph import visualize_knowledge_graph

# Page settings
st.set_page_config(page_title="Context-Aware QA with LLMs", layout="wide")
st.title(" Context-Aware QA for PDFs")

# --- Upload PDF ---
uploaded_file = st.file_uploader("📄 Upload a consulting PDF", type=["pdf"])
if uploaded_file:
    st.success(" PDF uploaded successfully!")

    # Read PDF directly from memory
    file_bytes = uploaded_file.read()
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    full_text = ""
    for page in doc:
        full_text += page.get_text()

    st.subheader(" Extracted Text Preview")
    st.text_area("Extracted Text", full_text[:2000], height=200)

    # --- LLM QA Section ---
    st.subheader(" Ask a Question")
    question = st.text_input("Type your question about this report:")
    if question:
        with st.spinner("Thinking..."):
            answer = ask_together_ai(question, full_text[:5000])
        st.markdown("** Answer:**")
        st.write(answer)

    # --- Knowledge Graph Section ---
    st.subheader("🔗 Knowledge Graph")
    st.markdown("This sample graph visualizes key ideas from the document.")
    sample_triples = [
        ("Generative AI", "has property", "Low-code"),
        ("Generative AI", "enables", "Productivity gains"),
        ("Generative AI", "poses risk", "Security issues"),
        ("Generative AI", "poses risk", "Bias"),
        ("Generative AI", "requires", "Human feedback"),
        ("Companies", "can fine-tune", "LLMs"),
        ("ChatGPT", "is an example of", "Generative AI")
    ]
    visualize_knowledge_graph(sample_triples)
