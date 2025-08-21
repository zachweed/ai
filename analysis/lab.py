#   The purpose of this is representing 
# two vectors in high-dimensional space.
# Mathematically, while anything >2 is
# high-dimensional (think complex plane),
# in vector math, we normally work with
# hundreds of dimensions as high-dimensional.
# 
#   Beyond that, technically the two points
# are two vectorized strings from Dictionary.

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import Dictionary

class Lab:
  def __init__(self, x1, x2):
    self.x1 = np.asarray(x1).ravel()
    self.x2 = np.asarray(x2).ravel()
    if self.x1.shape != self.x2.shape:
      raise ValueError(f"Shape mismatch: {self.x1.shape} vs {self.x2.shape}")

  def cosine(self) -> float:
    return float(_cosine_similarity(self.x1.reshape(1, -1), self.x2.reshape(1, -1))[0, 0])

  def euclidean(self):
    return float(np.linalg.norm(self.x1 - self.x2))