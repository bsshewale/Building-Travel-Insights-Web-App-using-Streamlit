from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def train_tfidf_model(text_data):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(text_data)
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    return vectorizer, cosine_sim
