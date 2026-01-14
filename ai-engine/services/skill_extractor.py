import json
import spacy
from functools import lru_cache
from pathlib import Path

@lru_cache(maxsize=1)
def load_nlp():
    return spacy.load("en_core_web_sm")

BASE_DIR = Path(__file__).resolve().parent.parent
SKILL_FILE = BASE_DIR / "models" / "skill_list.json"

with open(SKILL_FILE, "r", encoding="utf-8") as f:
    SKILLS = set(json.load(f))

def extract_skills(text: str):
    if not text:
        return []

    nlp = load_nlp()
    doc = nlp(text.lower())
    return list({t.text for t in doc if t.text in SKILLS})
