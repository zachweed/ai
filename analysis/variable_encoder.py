class VariableEncoder:
  def __init__(self, latent_dimensions = None):
    self.latent_dimensions = latent_dimensions

  # Supports various AutoEncoders
  def build(self, inputs, outputs = None):
    if outputs is None:
      return keras.Model(inputs, name = 'encoder')
    else:
      return keras.Model(inputs, outputs, name = 'encoder')

  def sampling(self, inputs):
    z_mean, z_log_variance = inputs
    epsilon = tf.random.normal(shape = (tf.shape(z_mean)[0], tf.shape(z_mean)[1]))
    return z_mean + tf.exp(0.5 * z_log_variance) * epsilon

  def build_variable_auto_encoder(self, inputs, features):
    flattened_features = keras.layers.Flatten()(features)
    z_mean = keras.layers.Dense(self.latent_dimensions, name = "z_mean")(flattened_features)
    z_log_variance = keras.layers.Dense(self.latent_dimensions, name = "z_log_variance")(flattened_features)
    z = keras.layers.Lambda(self.sampling)([z_mean, z_log_variance])
    return keras.Model(inputs, [z_mean, z_log_variance, z], name = 'variable_auto_encoder')
