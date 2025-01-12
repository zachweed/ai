import hashlib

from transformers import pipeline
from analysis.context import Context

class AskQuestion:
  def __init__(self, question, context, context_level):
    self.context_level = context_level
    self.question = question
    self.context = context
    self.answerer = pipeline(
      "question-answering", 
      model="distilbert-base-cased-distilled-squad"
    )

  def answer(self):
    result = self.answerer(question = self.question, context = self.build_context())
    print(f"\n{result['answer']}\n")

  def build_context(self):
    a = " ".join(Context().abbreviated_context(self.context_level))
    b = " ".join(self.context)
    return a + b

  def hash_context(self):
    encoded = self.context.encode("utf-8")
    hash_object = hashlib.md5(encoded)
    return hash_object.hex_digest
    
