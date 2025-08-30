import re
import joblib

from nltk.sentiment import *
from textblob import TextBlob
from analysis.context import Context
from analysis.ask_question import AskQuestion
from analysis.translation import Translation
from analysis.morpheme import Morpheme
from analysis.ensemble_sentiment import EnsembleSentiment

class Engine:
  def score(self, data):
    return TextBlob(data).sentiment.polarity

  def analyze_sentiment(self, data, simple=True):
    if simple:
      scores = []
      for token in Morpheme(data).tokens():
          scores.append(self.score(token))
      return scores
    else:
      model = joblib.load("data/sentiment_model.pkl")
      print(model.fit([data]))

  def extract_noun_phrases(self, data):
    return Morpheme(data).noun_phrases

  def translate(self, data):
    return Translation(data).translate

  def answer_question(self, question, context, context_level):
    return AskQuestion(question, context, context_level).answer()

