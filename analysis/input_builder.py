class InputBuilder:
  def __init__(self, inputs, layers):
    self.inputs = inputs
    self.layers = layers

  def build(self, training = None):
    x = self.inputs
    for layer in self.layers:
      try:
        x = layer(x, training = training)
      except TypeError:
        x = layer(x)
    return x