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

class Lab:
  def __init__(self, x1, x2):
    self.x1 = x1
    self.x2 = x2

  def cosine_similarity:
    return cosine_similarity([self.x1, self.x2])

  def euclidean_similarity:
    # i.e. euclidean distance
    return np.linalg.norm(self.x1 - self.x2)