from .layer import Layer
from .activation_functions import relu, relu_deriv


class NeuralNetwork:
  # dimensions is a list of ints
  def __init__(self, dimensions, activation_function=relu, activation_function_deriv=relu_deriv):
    self.dimensions = dimensions
    self.layers = [
      Layer(
        dimensions[i], dimensions[i+1] if i < len(dimensions) - 1 else 0,
        activation_function=activation_function,
        activation_function_deriv=activation_function_deriv
      )
      for i in range(len(dimensions))
    ]
    self.activation_function = activation_function
    self.activation_function_deriv = activation_function_deriv

  def forward_propagate(self, input):
    self.layers[0].set_neuron_values(input)
    for i in range(len(self.layers)-1):
      output = self.layers[i].forward_propagate()
      self.layers[i+1].set_neuron_values(output)
    return output.tolist()
  
  def deep_clone(self):
    nn_clone = NeuralNetwork(
      self.dimensions,
      activation_function=self.activation_function,
      activation_function_deriv=self.activation_function_deriv
    )
    layer_clones = [layer.deep_clone() for layer in self.layers]
    nn_clone.layers = layer_clones
    return nn_clone
