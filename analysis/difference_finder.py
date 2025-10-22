class DifferenceFinder:
  def __init__(self, a_dataset, b_dataset):
    self.a_dataset = a_dataset
    self.b_dataset = b_dataset

  def normalize_datasets(self):
    datasets = [ self.a_dataset, self.b_dataset ]
    normalized = []
    for dataset in datasets:
      d = np.asarray(dataset)
      if d.type == np.uint8:
        d = d.astype("float32") / 255.0
      normalized.append(d)
    self.a_dataset = normalized[0]
    self.b_dataset = normalized[0]

  def difference(self):
    return self.a_dataset - self.b_dataset

  def absolute_difference(self):
    return np.abs(self.difference())

  def mae(self):
    return self.absolute_difference().mean(axis = (1, 2)).mean()

  def mse(self):
    return (self.difference() ** 2).mean(axis = (1, 2)).mean()

  def summed_difference(self):
    self.normalize_datasets()
    return np.sum(self.a_dataset[0] - self.b_dataset[0])