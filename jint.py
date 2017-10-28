import sys
import nltk

from analysis.engine import Engine

for dep in ["vader_lexicon", "punkt"]: nltk.download(dep)

class Jint:
  def __init__(self, stream):
    self.data = stream

  def sentiment(self):
    return Engine().analyze_sentiment(self.data)
