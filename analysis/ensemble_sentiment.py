from typing import Iterable
import numpy as np

from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV
from sklearn.naive_bayes import ComplementNB
from sklearn.ensemble import StackingClassifier, VotingClassifier
from sklearn.model_selection import StratifiedKFold

class EnsembleSentiment(BaseEstimator, ClassifierMixin):
  def __init__(self, max_features: int = 5000, ngram_range: tuple = (1,2), use_voting_head: bool = True, cv_splits: int = 3, random_state: int = 42):
    self.max_features = max_features
    self.ngram_range = ngram_range
    self.use_voting_head = use_voting_head
    self.cv_splits = cv_splits
    self.random_state = random_state
    self._build_models()

  def _build_models(self):
    logistic_regression_clf = Pipeline([
      ("tfidf", TfidfVectorizer(max_features=self.max_features, ngram_range=self.ngram_range)),
      ("clf", LogisticRegression(max_iter=1000)),
    ])

    cv = StratifiedKFold(n_splits=self.cv_splits, shuffle=True, random_state=self.random_state)

    support_vector_machine = Pipeline([
      ("tfidf", TfidfVectorizer(max_features=self.max_features, ngram_range=self.ngram_range)),
      ("clf", CalibratedClassifierCV(estimator=LinearSVC(), method="sigmoid", cv=cv)),
    ])

    naive_bayes = Pipeline([
      ("tfidf", TfidfVectorizer(max_features=self.max_features, ngram_range=self.ngram_range)),
      ("clf", ComplementNB())
    ])

    self.base_estimators = [
      ("lr", logistic_regression_clf),
      ("svm", support_vector_machine),
      ("nb", naive_bayes)
    ]

    meta_learner = LogisticRegression(max_iter=1000, random_state=self.random_state)

    self.stacker = StackingClassifier(
      estimators = self.base_estimators,
      final_estimator = meta_learner,
      stack_method="auto",
      cv=cv,
      n_jobs=-1
    )

    if self.use_voting_head:
      voters = self.base_estimators + [("stack", self.stacker)]
      self.ensembler = VotingClassifier(estimators=voters, voting="hard", n_jobs=-1)
    else:
      self.ensembler = self.stacker

  def fit(self, X: Iterable[str], y: Iterable[str]):
    uniq, counts = np.unique(y, return_counts=True)
    min_class = counts.min()
    if self.cv_splits > min_class:
      self.cv_splits = max(2, min_class)
      self._build_models()
    self.ensembler.fit(X, y)
    return self

  def predict(self, X) -> np.ndarray:
    return self.ensembler.predict(X)

  def predict_proba(self, X: Iterable[str]) -> np.ndarray:
    if hasattr(self.ensembler, "predict_proba"):
      return self.ensembler.predict_proba(X)
    predictions = self.ensembler.predict(X)
    classes = getattr(self.ensembler, "classes_", None)
    probability = np.zeros((len(predictions), len(classes)))
    for i, c in enumerate(predictions):
      probability[i, classes == c] = 1.0
    return probability
