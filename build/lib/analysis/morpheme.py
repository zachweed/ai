import nltk
import nltk.tokenize

from textblob import TextBlob

class Morpheme:
  def __init__(self, analysis_string):
    self.chunk = analysis_string

  def tokens(self):
    return nltk.tokenize.sent_tokenize(self.chunk)

  def noun_phrases(self):
    return TextBlob(self.chunk).noun_phrases
