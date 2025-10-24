class Normalizer:
  @classmethod
  def normalize_float32(cls, original):
    return original.astype(np.float32) / 255.0