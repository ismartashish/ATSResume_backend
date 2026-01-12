import re
from collections import Counter

AI_PHRASES = [
    "results-driven",
    "goal-oriented",
    "highly motivated",
    "passionate",
    "detail-oriented",
    "dynamic professional",
    "leveraging my skills",
    "proven ability"
]

def detect_ai_content(text: str):
    warnings = []

    lowered = text.lower()

    for phrase in AI_PHRASES:
        if phrase in lowered:
            warnings.append(
                f"AI-style generic phrase detected: '{phrase}'"
            )

    return warnings
