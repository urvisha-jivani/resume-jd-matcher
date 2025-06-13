import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK data if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def clean_text(text):
    """Lowercase, remove non-word chars, tokenize, remove stopwords."""
    text = re.sub(r'\W+', ' ', text.lower())
    tokens = word_tokenize(text)
    tokens = [w for w in tokens if w not in stop_words]
    return ' '.join(tokens)

def compute_match_score(resume_text, jd_text):
    """Compute cosine similarity TF-IDF score between resume and JD."""
    clean_resume = clean_text(resume_text)
    clean_jd = clean_text(jd_text)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([clean_resume, clean_jd])

    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(score * 100, 2)
