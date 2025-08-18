import sklearn
from sklearn.feature_extraction.text import CountVectorizer

class Dictionary
  # Compute n-grams for a given string
  # Supports paragraphs and words
  def __init__(self, string):
    # {bi,tri}-grams over all characters, including whitespace 
    self.vectorizer = CountVectorizer(analyzer='char', ngram_range(2,3))
    self.x = self.vectorizer.fit_transform([string])
    self.features = self.vectorizer.get_feature_names_out()
    self.encoded_vector = x.toarray()

