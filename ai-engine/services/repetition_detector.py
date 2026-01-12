import re
from collections import Counter

def detect_repetition(text: str):
    words = re.findall(r"\b[a-zA-Z]{4,}\b", text.lower())

    common_words = Counter(words)
    repeated = []

    for word, count in common_words.items():
        if count >= 5:
            repeated.append({
                "word": word,
                "count": count
            })

    return repeated
