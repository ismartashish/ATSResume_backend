from sklearn.feature_extraction.text import TfidfVectorizer
from functools import lru_cache
import numpy as np

@lru_cache(maxsize=1)
def get_vectorizer():
    return TfidfVectorizer(stop_words="english")

def embed(text: str):
    """
    text: str
    returns: numpy.ndarray (1D vector)
    """
    vectorizer = get_vectorizer()
    vector = vectorizer.fit_transform([text]).toarray()
    return vector[0]
