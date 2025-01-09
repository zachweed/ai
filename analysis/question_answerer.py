from transformers import pipeline

class QuestionAnswerer:
  def answer_question(self, question, context):
    question_answerer = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
    result = question_answerer(question=question, context=context)
    print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")
