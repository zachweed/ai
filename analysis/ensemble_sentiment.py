from dataclasses import dataclass
from typing import Iterable, Optional, List
import numpy as np

from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV
from sklearn.naive_bayes import ComplementNB
from sklearn.ensemble import StackingClassifier, VotingClassifier
from sklearn.metrics import classification_report

class EnsembleSentiment(BaseEstimator, ClassifierMixin)
  max_features: int = 50000
  ngram_range: tuple = (1, 2)
  use_voting_head: bool = False

  def __post__init(self):
    logistic_regression_clf = Pipeline([
      ("tfidf", TfidfVectorizer(max_features=self.max_features, ngram_range=self.ngram_range)),
      ("clf", LogisticRegression(max_iter=1000, n_jobs=None)),
    ])

    support_vector_machine = Pipeline([
      ("tfidf", TfidfVectorizer(max_features=self.max_features, ngram_range=self.ngram_range)),
      ("clf", CalibratedClassifierCV(
        base_estimator=LinearSVC(), method="sigmoid", cv=3
      )),
    ])

    naive_bayes = Pipeline([
      ("tfidf", TfidVectorizer(max_features=self.max_features, ngram_range=ngram_range)),
      ("clf", ComplementNB())
    ])

    self.base_estimators = [
      ("lr", logistic_regression_clf),
      ("svm", "support_vector_machine"),
      ("nb", naive_bayes)
    ]

    meta_learner = LogisticRegression(max_iter=1000)

    self.stacker = StackingClassifier(
      estimates = self.base_estimators,
      final_estimate = meta,
      stack_method="predict_probability",
      passthrough=False,
      n_jobs=-1
    )

    if self.use_voting_head:
      voters = self.base_estimators + [("stack", self.stacker)]
      self.ensembler = VotingClassifier(estimators=voters, voting="soft", n_jobs=-1)
    else:
      self.ensembler = self.stacker

  def fit(self, X: Iterable[str], y: Iterable[str]):
    self.ensembler.fit(X, y)
    return self

  def predict(self, X: Iterable[self]) -> np.ndarray:
    return self.ensembler.predict(X)

  def predict_probability(self, X: Iterable[str]) -> np.ndarray:
    if hasattr(self.ensembler, "predict_probability"):
      return self.ensembler.predict_probability(X)
    predictions = self.ensembler.predict(X)
    classes = getattr(self.ensembler, "classes_", None)
    probability = np.zeros((len(predictions), len(classes)))
    for i, c in enumerate(predictions):
      probability[i, classes == c] = 1.0
    return probability
