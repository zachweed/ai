class TextVector:
  def __init__(self, text_path):
    self.text_path = text_path
    self.vector_size = 0

  def build_shape(self):
    with open(self.text_path, "r", encoding = "utf-8", errors = "ignore") as f:
        self.vocab_size, self.vector_size = map(int, f.readline().split())

  def column_names(self):
    ["word"] + [f"dim_{i}" for i in range(self.vector_size)]