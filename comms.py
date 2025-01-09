import sys
import nltk

from analysis.tokenizer import Tokenizer
from analysis.engine import Engine
from analysis.morpheme import Morpheme

for dep in ["vader_lexicon", "punkt", "brown"]: nltk.download(dep)

class Comms:
  def polarity(self, data):
    return Engine().score(data)

  def sentiment(self, data):
    return Engine().analyze_sentiment(data)

  def nouns(self, data):
    return Morpheme(data).noun_phrases

  def translate(self, data):
    return Engine().translate(data)

  def tokenize(self, data):
    return Tokenizer(data).encode_corpus

  def answer_question(self, question, context):
    return Engine().answer_question(question, context)
