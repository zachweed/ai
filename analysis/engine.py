import re

from analysis.translation import Translation
from analysis.morpheme import Morpheme
from nltk.sentiment import *
from textblob import TextBlob

class Engine:
  def score(self, data):
    return TextBlob(data).sentiment.polarity

  def analyze_sentiment(self, data):
    scores = []
    for token in Morpheme(data).tokens():
        scores.append(self.score(token))
    return scores

  def extract_noun_phrases(self, data):
    return Morpheme(data).noun_phrases

  def translate(self, data):
    return Translation(data).translate

