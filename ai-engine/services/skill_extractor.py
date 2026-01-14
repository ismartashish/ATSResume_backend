import json
import spacy
import subprocess
import sys
from functools import lru_cache
from pathlib import Path

# -----------------------------
# SAFE MODEL LOADER (AUTO FIX)
# -----------------------------
@lru_cache(maxsize=1)
def load_nlp():
    try:
        return spacy.load("en_core_web_sm")
    except OSError:
        # Auto-download if missing (Render / fresh deploy)
        subprocess.check_call(
            [sys.executable, "-m", "spacy", "download", "en_core_web_sm"]
        )
        return spacy.load("en_core_web_sm")


# -----------------------------
# LOAD SKILLS (PATH SAFE)
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
SKILL_FILE = BASE_DIR / "models" / "skill_list.json"

with open(SKILL_FILE, "r", encoding="utf-8") as f:
    SKILLS = set(json.load(f))


# -----------------------------
# EXTRACT SKILLS
# -----------------------------
def extract_skills(text: str):
    if not text:
        return []

    nlp = load_nlp()
    doc = nlp(text.lower())

    return list({token.text for token in doc if token.text in SKILLS})
