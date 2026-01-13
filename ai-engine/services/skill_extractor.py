import spacy
import json
from functools import lru_cache

# Load skills list once (this is cheap)
with open("models/skill_list.json") as f:
    SKILLS = set(json.load(f))


@lru_cache(maxsize=1)
def get_nlp():
    """
    Lazy-load spaCy model.
    Loads only on first request, not at startup.
    """
    return spacy.load("en_core_web_sm")


def extract_skills(text: str):
    nlp = get_nlp()
    doc = nlp(text.lower())

    found = set()
    for token in doc:
        if token.text in SKILLS:
            found.add(token.text)

    return list(found)
