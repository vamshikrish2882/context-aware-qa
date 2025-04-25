# src/entity_extractor.py

import spacy

# Load the English NLP pipeline
nlp = spacy.load("en_core_web_sm")

def extract_named_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

if __name__ == "__main__":
    # Load the text from BCG document
    with open("bcg_ai_guide.txt", "r", encoding="utf-8") as f:
        text = f.read()

    entities = extract_named_entities(text)

    # Show a few results
    for ent in entities[:30]:
        print(ent)
