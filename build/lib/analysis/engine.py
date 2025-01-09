import re

import gradio as gr
from transformers import TFAutoModelForSeq2SeqLM
from transformers import AutoTokenizer
from analysis.morpheme import Morpheme
from nltk.sentiment import *
from textblob import TextBlob

class Engine:
  def __init__(self):
    self.engine = SentimentIntensityAnalyzer()

  # Aliased polarity scores, as aggregates
  # of overall sentiment from sentence.
  def score(self, data):
    return TextBlob(data).sentiment.polarity

  def analyze_sentiment(self, data):
    scores = []
    for token in Morpheme(data).tokens():
        scores.append(self.score(token))
    return scores

  def extract_noun_phrases(self, data):
    return Morpheme(data).noun_phrases

  def answer_question(self, question, context):
    question_answerer = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
    result = question_answerer(question=question, context=context)
    print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")

  def translate(self, data):
    string = re.search("(.*):(.*)", data)
    # Represents like 'please translate from:'
    translation_request = string[0]
    # Represents what to translate
    for_translation = string[2]
    tokenizer = AutoTokenizer.from_pretrained("t5-base")
    translation_model = TFAutoModelForSeq2SeqLM.from_pretrained("t5-base")
    inputs = tokenizer(f"{translation_request}: {for_translation}", return_tensors="tf").input_ids
    outputs = translation_model.generate(inputs)
    tokenizer.decode(ouputs[0], skip_special_tokens=True)

