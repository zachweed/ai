# Handles common tasks for building a PCA
class AnalogyPCAHelper:
  def __init__(self, n_components = 2, random_state = 0):
    self.scaled = StandardScaler()
    self.pca = PCA(n_components = n_components, random_state  random_state)
    self.features = []

  # Fit numeric columns
  def fit(self, X, drop_columns):
    numeric_columns = X.select_dtypes(include = "number").copy()
    if drop_columns:
        numeric_columns = numeric_columns.drop(columns = list(drop_columns), errors = "ignore")
    self.features = list(numeric_columns)
    transformed = self.scaler.fit_transform(numeric_columns.values)
    self.pca.fit(transformed)
    return self

  # Project a Panda as a 2D PCA
  def transform(self, X):
    numeric_columns = X[self.features].astype(float).values
    numeric_scaled = self.scaler.transform(numeric_columns)
    transformed = self.pca.transform(numeric_scaled)
    return pd.DataFrame(transformed, columns = ["PCA_Dimension_1", "PCA_Dimension_2"], index = X.index)

  def _standardize_vector(self, x):
    if isinstance(x, pd.Series):
      v = x[self.features].astype(float).values
    elif isinstance(x, dict):
      v = np.asarray([x[c] for c in self.features], dtype = float)
    else:
      v = np.asarray(x, dtype = float)
    return self.scaler.transform(v.reshape(1, -1))[0]

  # Standardize points for purpose of
  # projecting along PCA axes
  def _standardize_for_pca2(self, z):
    return (z @ self.pca.components_.T)[:2]

  def project_points(self, points):
    output = {}
    for name, point in points.items():
      z = self.standardize_vector(point)
      output[name] = self._standardize_for_pca2(z)
    return pd.DataFrame(output, index = ["PCA_Dimension_1", "PCA_Dimension_2"]).T
