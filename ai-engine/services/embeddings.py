from sklearn.feature_extraction.text import TfidfVectorizer
from functools import lru_cache
import numpy as np


@lru_cache(maxsize=1)
def get_vectorizer():
    return TfidfVectorizer(stop_words="english")


def embed(texts):
    """
    texts: list[str]
    returns: numpy array
    """
    vectorizer = get_vectorizer()
    return vectorizer.fit_transform(texts).toarray()
