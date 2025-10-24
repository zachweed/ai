# Building variables with the full
# clean dataset, as X_train_clean and
# X_valid_clean are disjoint, thus this
# provides us with a 1:1 mapping of indices
class DatasetCloner:
  def __init__(self, original_dataset, sample_size):
    begin_range = len(original_dataset)
    self.clone = original_dataset.copy()
    self.train_clone = self.clone[np.arange(0, begin_range - sample_size)]
    self.validation_clone = self.clone[np.arange(begin_range - sample_size, begin_range)]