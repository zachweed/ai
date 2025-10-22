# Does quantified analysis of the images
class DifferenceFinder:
  def __init__(self, a_dataset, b_dataset):
    self.a_dataset = a_dataset
    self.b_dataset = b_dataset

  def normalize_datasets(self):
    datasets = [self.a_dataset, self.b_dataset]
    normalized = []
    for dataset in datasets:
      d = np.asarray(dataset)
      if d.dtype == np.uint8:
        d = d.astype("float32") / 255.0
      normalized.append(d)
    self.a_dataset = normalized[0]
    self.b_dataset = normalized[1]

  def difference(self):
    return self.a_dataset - self.b_dataset

  def absolute_difference(self):
    return np.abs(self.difference())

  def per_image_mae(self):
    axes = tuple(range(1, self.a_dataset.ndim))
    return self.absolute_difference().mean(axis = axes)

  def mean_mae(self):
    return float(self.per_image_mae().mean())

  def per_image_mse(self):
    axes = tuple(range(1, self.a_dataset.ndim))
    return (self.difference() ** 2).mean(axis = axes)

  def mean_mse(self):
    return (self.difference() ** 2).mean(axis = (1, 2)).mean()

  def summed_difference(self):
    d = self.difference()
    axes = tuple(range(1, d.ndim))
    return d.sum(axis = axes)
