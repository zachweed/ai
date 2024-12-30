from analysis.morpheme import Morpheme
from nltk.sentiment import *
from textblob import TextBlob

class Engine:
  def __init__(self):
    self.engine = SentimentIntensityAnalyzer()

  # Aliased polarity scores, as aggregates
  # of overall sentiment from sentence.
  def score(self, content):
    return self.engine.polarity_scores(content)

  def analyze_sentiment(self, data):
    scores = []
    for token in Morpheme(data).tokens():
        scores.append(self.score(token))
    return scores

  def extract_noun_phrases(self, data):
    return Morpheme(data).noun_phrases

