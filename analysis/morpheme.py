import nltk
import nltk.tokenize

class Morpheme:
  def __init__(self, analysis_string):
    self.chunk = analysis_string

  def tokens(self):
    return nltk.tokenize.sent_tokenize(self.chunk)
