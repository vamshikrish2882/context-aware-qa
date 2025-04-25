# 🧠 Context-Aware QA System with LLMs and Knowledge Graphs

This Streamlit app enables users to **upload consulting reports (PDFs)** and interactively:
- 🤖 Ask **contextual questions** using Together AI's LLM (Mixtral)
- 🔎 Explore insights using a **mini knowledge graph**
- 📄 Understand documents faster through **LLM-driven summarization and reasoning**

Built for generative AI applications in organizational memory, strategic insights, and NLP workflows.

---

## 🚀 Features

- **PDF Upload**: Drag and drop any business, consulting, or research report
- **LLM-Based QA**: Ask natural language questions using Together AI's Mixtral-8x7B-Instruct model
- **Text Extraction**: Clean, fast PDF parsing with PyMuPDF
- **Knowledge Graph Visualization**: See key concepts and their relationships
- **Streamlit UI**: Intuitive and lightweight web interface

---

## 🖥️ Live Demo

🔗 Coming soon on **Streamlit Cloud**

---

## 📁 Project Structure

context-aware-qa/ ├── app.py # Main Streamlit app ├── requirements.txt # All dependencies ├── .env.template # API key template for Together AI ├── .gitignore # To ignore venv, .env, etc. └── src/ ├── qa_llm.py # LLM-powered QA logic ├── knowledge_graph.py # Knowledge graph visualization └── entity_extractor.py # Named entity recognition (optional)

yaml
Copy
Edit

---

## ⚙️ Getting Started Locally

### 1. Clone the repo

```bash
git clone https://github.com/vamshikrish2882/context-aware-qa.git
cd context-aware-qa
2. Set up virtual environment
bash
Copy
Edit
python -m venv venv
.\venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
python -m spacy download en_core_web_sm
4. Add your .env file
Create a .env with your Together AI API key:

ini
Copy
Edit
TOGETHER_API_KEY=your_key_here
5. Run the app
bash
Copy
Edit
streamlit run app.py
Open in browser at: http://localhost:8501

🤝 Credits
LLM: Together AI

NLP: spaCy

Visualization: NetworkX + Matplotlib

Frontend: Streamlit

📬 Contact
Vamshikrishna Pandilla
LinkedIn | GitHub

🧪 Use Case
Built for internship with Experio — simulates real-world knowledge-driven AI for consulting workflows.

yaml
Copy
Edit

---

Once you've pasted this into `README.md`, just do:
```bash
git add README.md
git commit -m "Add README for project documentation"
git push
