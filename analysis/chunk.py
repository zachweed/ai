import nltk

from nltk import tokenize

class Chunk:
    def __init__(self, analysis_string):
        self.chunk = analysis_string

    def tokens(self):
        return nltk.sent_tokenize(self.chunk)
