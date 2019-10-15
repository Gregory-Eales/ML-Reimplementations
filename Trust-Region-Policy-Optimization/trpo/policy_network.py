import torch
import numpy as np


class PolicyNetwork(object):

    def __init__(self, alpha, input_size, output_size):

        self.input_size = input_size
        self.output_size = output_size

        self.fc1 = torch.nn.Linear(input_size, 128)
        self.fc2 = torch.nn.Linear(128, 128)
        self.fc3 = torch.nn.Linear(128, output_size)
        self.tanh = torch.nn.Tanh()
        self.relu = torch.nn.LeakyReLU()

        self.optimizer = torch.optim.Adam(lr=alpha)

        self.device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu:0')
        self.to(self.device)

    def loss(self):
        pass

    def forward(self, x):
        x = x.to(self.device)
        out = self.fc1(x)
        out = self.tanh(out)
        out = self.fc2(out)
        out = self.tanh(out)
        out = self.fc3(out)
        out = self.relu(out)
        out = out.to(torch.device('cpu:0'))

    def optimize(self, iterations=1):
        pass
