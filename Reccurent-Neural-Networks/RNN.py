import torch

class RNN(object):

    def __init__(self, x_shape, y_shape):
        
        # init dense params
        self.dense_w = {}
        self.dense_z = {}
        self.dense_b = {}
        self.dense_a = {}

        # init reccurent params
        self.rec_w = {}
        self.rec_z = {}
        self.rec_b = {}
        self.rec_a = {}

    def initialize_weights(self):
        pass

    def init_reccurent_weights(self):
        pass

    def init_dense_weights(self):
        pass

    def single_reccurent(self):
        pass

    def reccurent_forward(self):
        pass

    def dense_forward(self):
        pass

    def reccurent_backward(self):
        pass