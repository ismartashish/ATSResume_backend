import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SKILL_FILE = BASE_DIR / "models" / "skill_list.json"

with open(SKILL_FILE, "r", encoding="utf-8") as f:
    SKILLS = set(json.load(f))

def extract_skills(text: str):
    if not text:
        return []

    text = text.lower()
    words = re.findall(r"[a-zA-Z+#.]+", text)

    return list({w for w in words if w in SKILLS})
