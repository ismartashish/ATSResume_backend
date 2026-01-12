import spacy
import json

nlp = spacy.load("en_core_web_sm")

with open("models/skill_list.json") as f:
    SKILLS = set(json.load(f))

def extract_skills(text: str):
    doc = nlp(text.lower())
    found = set()

    for token in doc:
        if token.text in SKILLS:
            found.add(token.text)

    return list(found)
