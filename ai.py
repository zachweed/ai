import sys
import nltk

for dep in ["vader_lexicon", "punkt", "brown"]: nltk.download(dep)

from analysis.context import Context
from analysis.tokenizer import Tokenizer
from analysis.engine import Engine
from analysis.morpheme import Morpheme

class Ai:
  def polarity(self, data):
    return Engine().score(data)

  def sentiment_scores(self, data):
    return Engine().analyze_sentiment(data)

  def overall_sentiment(self, data):
    return Engine().analyze_sentiment(data, scored=False)

  def nouns(self, data):
    return Morpheme(data).noun_phrases

  def translate(self, data):
    return Engine().translate(data)

  def tokenize(self, data):
    return Tokenizer(data).encode_corpus

  def answer_question(self, question, context, context_level):
    return Engine().answer_question(question, context, context_level)
