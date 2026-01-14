from sklearn.feature_extraction.text import TfidfVectorizer

def embed_pair(text1: str, text2: str):
    """
    Fit TF-IDF on BOTH texts together.
    Returns two vectors in the SAME vector space.
    """
    vectorizer = TfidfVectorizer(stop_words="english")

    vectors = vectorizer.fit_transform([text1, text2]).toarray()

    return vectors[0], vectors[1]
