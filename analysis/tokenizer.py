class Tokenizer:
  def __init__(self, corpus):
    self.corpus = corpus
    self.bag_of_words = {}

  def encode_corpus(self):
    words = self.corpus.split(" ")
    for word in words:
      if word not in self.bag_of_words:
        self.bag_of_words[word] = len(self.bag_of_words) + 1
    return self.bag_of_words
