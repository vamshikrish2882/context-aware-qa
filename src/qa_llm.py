import requests
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

def ask_together_ai(question, context):
    url = "https://api.together.xyz/inference"
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""Answer the question based on the context below.

Context:
{context}

Question: {question}
Answer:"""

    payload = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "prompt": prompt,
        "max_tokens": 300,
        "temperature": 0.5,
        "top_p": 0.9,
    }

    response = requests.post(url, headers=headers, json=payload)
    print(" Status:", response.status_code)

    if response.status_code != 200:
        print(" Response Text:", response.text)
        return " Request failed."

    try:
        result = response.json()
        print("🧾 FULL JSON Response:", result)  # Optional debug
        return result["choices"][0]["text"].strip()
    except Exception as e:
        return f" Error parsing response: {e}"

if __name__ == "__main__":
    with open("bcg_ai_guide.txt", "r", encoding="utf-8") as f:
        context = f.read()

    question = input("Ask a question: ")
    answer = ask_together_ai(question, context[:5000])
    print("\n Answer:", answer)
