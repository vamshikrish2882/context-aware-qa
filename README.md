# 🧠 Context-Aware QA System

A lightweight Streamlit app that lets users:
- Upload PDFs (e.g. consulting reports)
- Ask questions using LLMs (Together AI - Mixtral)
- Visualize key concepts in a knowledge graph

This project simulates how LLMs and knowledge graphs can power AI tools for consulting and enterprise search.

---

## 🚀 Key Features

- 📄 **PDF Upload**: Add any report and extract clean text
- 🤖 **Question Answering**: Ask custom questions using Together AI’s Mixtral LLM
- 🧠 **Knowledge Graph**: Visualize entities and relationships from the content
- 🧰 **Tech Stack**: Python, Streamlit, spaCy, NetworkX, Together AI

---

## 💻 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/vamshikrish2882/context-aware-qa.git
cd context-aware-qa

# 2. Create virtual environment
python -m venv venv
.\venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

# 4. Add your Together AI API key
echo TOGETHER_API_KEY=your_key_here > .env

# 5. Run the app
streamlit run app.py
