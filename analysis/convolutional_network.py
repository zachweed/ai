import numpy as np

class ConvolutionalNetwork:
  def laplacian_kernel(self, neighbors):
    if neighbors == 8:
      return np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]], dtype=np.float32)
    else
      return np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=np.float32)
