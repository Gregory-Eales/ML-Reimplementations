import torch as tf

class CNN(object):

    # TO DO:
    # - initalize dense weights
    # - initialize conv weights
    # - initalize pool weights lol :)
    # - single conv
    # - single pool
    # - conv forward
    # - dense forward
    # - pool forward
    # - conv backward
    # - dense backward

    def __init__(self, dense_length, conv_length, x_shape, y_shape):

        # conv_length = the number of convolutional layers
        # dense_length = the number of dense layers
        # x_shape = the shape of the input data
        # y_shape = the shape of the output data
        
        # init params
        self.dense_length = dense_length
        self.conv_length = conv_length
        self.x_shape = x_shape
        self.y_shape = y_shape

        # initalize weights
        self.dense_w = {}
        self.conv_w = {}

        # initialize z
        self.dense_z = {}
        self.conv_z = {}
        self.pool_z = {}

        # initialize activations
        self.dense_a = {}
        self.conv_a = {}
        self.pool_a = {}

        # run intialization functions
        self.initialize_weights()


    def initialize_dense_weights(self):
        
        # need output shape of last conv layer
        output = self.conv_w["w" + str(self.conv_length)].numel()

        self.dense_w["w1"] = tf.rand(output, y.shape[1] + 1)

        for i in range(2, self.dense_length+1):
            
            if i != self.dense_length:
                self.dense["w"+str(i)] = tf.rand(y.shape[1]+1, y.shape[1]+1)

            else:
                self.dense["w"+str(i)] = tf.rand(y_shape[1]+1, y_shape[1])

    def initialize_conv_weights(self):
        
        for i in range(self.conv_length):
            self.conv_w["w" + str(i+1)] = tf.rand(64/(2**i), 3, 3)

    def initialize_weights(self):
        self.initialize_conv_weights()
        self.initialize_dense_weights()

    def single_conv(self, z, w, activation="tanh"):
        
        if activation == "tanh":
            return tf.tanh(tf.sum(z*w))

        if activation == "relu":
            return tf.nn.functional.relu(tf.sum(z*w))

        if activation == "sigmoid":
            return tf.sigmoid(tf.sum(z*w))

    def single_avg_pool(self, z, kernal_size=3, activation="tanh"):

        if activation == "tanh":
            return tf.tanh(tf.sum(z)/kernal_size**2)

        if activation == "relu":
            return tf.nn.functional.relu(tf.sum(z)/kernal_size**2)

        if activation == "sigmoid":
            return tf.sigmoid(tf.sum(z)/kernal_size**2)
        

    def conv_forward(self):
        pass

    def pool_forward(self):
        pass

    def dense_forward(self):
        pass

    def conv_backward(self):
        pass

    def dense_backward(self):
        pass