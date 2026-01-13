from sklearn.feature_extraction.text import TfidfVectorizer

def embed(texts):
    """
    texts: list[str]
    returns: numpy.ndarray
    """
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(texts)
    return vectors.toarray()
