import json
import spacy
from functools import lru_cache

@lru_cache(maxsize=1)
def load_nlp():
    return spacy.load("en_core_web_sm")

with open("models/skill_list.json") as f:
    SKILLS = set(json.load(f))

def extract_skills(text: str):
    nlp = load_nlp()
    doc = nlp(text.lower())

    return list({token.text for token in doc if token.text in SKILLS})
