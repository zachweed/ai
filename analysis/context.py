import nltk

from nltk.corpus import brown

class Context:
  BOUNDARY = 1000000

  def abbreviated_context(self, level):
    print(f"boundary of {level}")
    if level == 'high':
      boundary = round(self.BOUNDARY)
    elif level == 'medium':
      boundary = round(self.BOUNDARY / 2)
    elif level == 'low':
      boundary = round(self.BOUNDARY / 4)
    return brown.words()[:boundary]


