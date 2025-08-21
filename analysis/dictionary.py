import sklearn
from sklearn.feature_extraction.text import CountVectorizer

class Dictionary:
  # Compute n-grams for a given string
  # Supports paragraphs and words
  def __init__(self, vectorizer=None, *, ngram_range=(2,3), lowercase=True):
    self.vectorizer = vectorizer or CountVectorizer(analyzer='char', ngram_range=(2,3), lowercase=lowercase)
    self.features = None

  def fit(self, text: str):
    X = self.vectorizer.fit_transform([text])
    self.features = self.vectorizer.get_feature_names_out()
    self.encoded_vector = X.toarray()[0]
    return self

  def transform(self, text: str) -> np.ndarray:
    return self.vectorizer.transform([text]).toarray()[0]
