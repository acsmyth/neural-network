import numpy as np
from activation_functions import relu, relu_deriv


class Layer:
	def __init__(self, num_neurons, next_layer_num_neurons, activation_function=relu, activation_function_deriv=relu_deriv):
		self.neuron_matrix = np.zeros((num_neurons, 1))
		self.weights_matrix = np.random.rand(num_neurons, next_layer_num_neurons)
		self.biases_matrix = np.random.rand(next_layer_num_neurons)
		self.activation_function = activation_function
		self.activation_function_deriv = activation_function_deriv

	def forward_propagate(self):
		output_neurons = np.dot(self.weights_matrix.transpose(), self.neuron_matrix)
		output_neurons = np.add(output_neurons, self.biases_matrix)
		output_neurons = self.activation_function(output_neurons)
		return output_neurons

	def set_neuron_values(self, neuron_values):
		self.neuron_matrix = np.array(neuron_values)
