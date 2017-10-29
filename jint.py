import sys
import nltk

from analysis.engine import Engine

for dep in ["vader_lexicon", "punkt"]: nltk.download(dep)

class Jint:
  def sentiment(self, data):
    return Engine().analyze_sentiment(data)
