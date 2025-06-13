import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download stopwords if not already present
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def clean_text(text):
    """
    Lowercase, remove non-word characters, split into words,
    and remove common English stopwords.
    """
    text = re.sub(r'\W+', ' ', text.lower())
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

def compute_match_score(resume_text, jd_text):
    """
    Compute a similarity score (0-100) between resume and job description
    using TF-IDF vectorization and cosine similarity.
    """
    clean_resume = clean_text(resume_text)
    clean_jd = clean_text(jd_text)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([clean_resume, clean_jd])

    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(score * 100, 2)
