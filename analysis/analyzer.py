import morpheme

from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import *

class Analyzer:
    def __init__(self):
        self.engine = SentimentIntensityAnalyzer()

    def score(self, content):
        return self.engine.polarity_scores(content)

    def analyze_sentiment(self, data):
        scores = []
        for token in morpheme.Morpheme(data).tokens():
            scores.append(self.score(token))
        return scores

