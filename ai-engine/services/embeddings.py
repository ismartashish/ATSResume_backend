from sentence_transformers import SentenceTransformer

# Load model once (important for performance)
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed(text: str):
    """
    Convert text into sentence embedding
    """
    return model.encode(text)
