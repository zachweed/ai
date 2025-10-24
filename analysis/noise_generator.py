# Helper class responsible for generating noise on a given dataset
class NoiseGenerator:
  @classmethod
  def call(dataset, noise_level):
    rng = np.random.default_rng(42)
    return np.clip(dataset + noise_level * rng.normal(size = dataset.shape), 0, 1)
