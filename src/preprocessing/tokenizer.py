import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

def tokenize(text):
    """Tokenizes the input text into words."""
    # Lowercase the text
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenize the text
    tokens = word_tokenize(text)
    return tokens

def remove_stopwords(tokens):
    """Removes stopwords from the list of tokens."""
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    return filtered_tokens

def tf(tokens):
    """Calculates term frequency for the tokens."""
    token_count = Counter(tokens)
    total_tokens = len(tokens)
    tf_scores = {token: count / total_tokens for token, count in token_count.items()}
    return tf_scores

def df(corpus):
    """Calculates document frequency for the tokens in the corpus."""
    df_scores = {}
    total_docs = len(corpus)
    for tokens in corpus:
        unique_tokens = set(tokens)
        for token in unique_tokens:
            if token in df_scores:
                df_scores[token] += 1
            else:
                df_scores[token] = 1
    df_scores = {token: count / total_docs for token, count in df_scores.items()}
    return df_scores

def tf_idf(corpus):
    """Calculates TF-IDF scores for the tokens in the corpus."""
    tf_scores = [tf(tokens) for tokens in corpus]
    df_scores = df(corpus)
    tf_idf_scores = []
    for tf_score in tf_scores:
        tf_idf = {token: tf_score[token] * df_scores.get(token, 0) for token in tf_score}
        tf_idf_scores.append(tf_idf)
    return tf_idf_scores