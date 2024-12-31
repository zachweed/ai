import re

from transformers import TFAutoModelForSeq2SeqLM
from transformers import AutoTokenizer
from textblob import TextBlob

class Translation:
  def __init__(self, data):
    self.data = data
    self.tokenizer = AutoTokenizer.from_pretrained("t5-base")
    self.translation_model = TFAutoModelForSeq2SeqLM.from_pretrained("t5-base")

  def build_query_string(self, data):
    string = re.search("(.*):(.*)", self.data)
    return [string[1], string[2]]

  def translate(self):
    query_string = self.build_query_string(self.data)
    inputs = self.tokenizer(f"{query_string[0]}: {query_string[1]}", return_tensors="tf").input_ids
    outputs = self.translation_model.generate(inputs)
    return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

