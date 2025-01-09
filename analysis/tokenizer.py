class Tokenizer:
  def __init__(self, corpus):
    self.corpus = corpus
    self.bag_of_words = {}

  def split_sentences(self):
    sentences = self.corpus.split(".")
    sentences.remove("")
    return sentences

  def split_words(self, data):
    words = data.split(" ")

  def encode_corpus(self):
    encoded_words = []
    sentences = self.split_sentences()
    for sentence in sentences:
      encoded_words.append([])
      words = self.split_words(sentence)
      for word in words:
        if word not in self.bag_of_words:
          self.bag_of_words[word] = len(self.bag_of_words) + 1
        encoded_words[len(encoded_words) - 1].append(self.bag_of_words[word])
    return encoded_words
