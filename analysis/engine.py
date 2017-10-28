from analysis.morpheme import Morpheme

from nltk.sentiment import *

class Engine:
  def __init__(self):
    self.engine = SentimentIntensityAnalyzer()

  def score(self, content):
    return self.engine.polarity_scores(content)

  def analyze_sentiment(self, data):
    scores = []
    for token in Morpheme(data).tokens():
        scores.append(self.score(token))
    return scores

