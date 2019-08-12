import numpy as np
import torch

# neural network class
class NeuralNetwork(object):

	def __init__(self, input_shape=1, output_shape=1, num_layers=3, gpu=False):

		# check for correct input types and values
		assert type(input_shape) == int, "input shape needs to be an integer"
		assert input_shape > 0, "input shape needs to be greater than 0"

		assert type(output_shape) == int, "input type needs to be an integer"
		assert output_shape > 0, "output shape needs to be greater than 0"

		assert type(num_layers) == int, "number of layers needs to be an integer"
		assert num_layers >= 3, "number of layers needs to be 3 or larger"

		assert type(gpu) == bool, "type of gpu needs to be bool"

		# internalize network parameters
		self.gpu = gpu
		self.input_shape = input_shape
		self.output_shape = output_shape
		self.num_layers = num_layers

		# create variables
		self.w = None
		self.b = None
		self.z = None
		self.a = None

		# initialize weight cache
		self.initialize_weights()
		# initialize bias cache
		self.initialize_bias()
		# initialize activation cache
		self.initialize_activations()
		# initialize z cache
		self.initialize_z()

	def initialize_weights(self):

		self.w = {}

		for i in range(1, self.num_layers):

			# use pytorch if gpu is true
			if self.gpu == True:

				if (self.num_layers-1) == i:
					self.w["w" + str(i)] = torch.randn(self.input_shape+1, self.output_shape, dtype=torch.float16)

				if (self.num_layers-1) != 1:
					self.w["w" + str(i)] = torch.randn(self.input_shape, self.input_shape+1, dtype=torch.float16)

				else:
					self.w["w" + str(i)] = torch.randn(self.input_shape+1, self.input_shape+1, dtype=torch.float16)

			# use numpy if gpu is false
			if self.gpu == False:

				if (self.num_layers-1) == i:
					self.w["w" + str(i)] = np.randn(self.input_shape+1, self.output_shape, dtype=torch.float16)
					self.w["w" + str(i)] = self.w["w" + str(i)].astype('float64') 

				if (self.num_layers-1) != 1:
					self.w["w" + str(i)] = np.randn(self.input_shape, self.input_shape+1, dtype=torch.float16)

				else:
					self.w["w" + str(i)] = np.random.random(self.input_shape+1, self.input_shape+1, dtype=torch.float16)



	def initialize_bias(self):

		self.b = {}

		for i in range(1, self.num_layers):

			# use pytorch if gpu is true
			if self.gpu == True:
				self.b["b" + str(i)] = torch.randn(5, 7, dtype=torch.float16)


			# use numpy if gpu is false
			if self.gpu == False:
				self.b["b" + str(i)] = np.random.random(size=None)



	def initialize_activations(self):
		self.a = {}

		for i in range(1, self.num_layers):

			# use pytorch if gpu is true
			if self.gpu == True:
				self.a["a" + str(i)] = torch.randn(5, 7, dtype=torch.float16)


			# use numpy if gpu is false
			if self.gpu == False:
				self.a["a" + str(i)] = np.random.random(size=None)



	def initialize_z(self):

		self.z = {}

		for i in range(1, self.num_layers):

			# use pytorch if gpu is true
			if self.gpu == True:
				self.z["z" + str(i)] = torch.randn(5, 7, dtype=torch.float16)

			# use numpy if gpu is false
			if self.gpu == False:
				self.w["w" + str(i)] = np.random.random(size=None)
