from sentence_transformers import SentenceTransformer, util

# Load the pre-trained SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_match_score(resume_text, jd_text):
    """
    Compute a semantic similarity score (0–100) between resume and job description
    using BERT embeddings and cosine similarity.
    """
    embeddings = model.encode([resume_text, jd_text], convert_to_tensor=True)
    cosine_sim = util.pytorch_cos_sim(embeddings[0], embeddings[1]).item()
    return round(cosine_sim * 100, 2)
