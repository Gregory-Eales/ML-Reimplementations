import torch

class PolicyNetwork(torch.nn.Module):

    def __init__(self, alpha, input_dims, output_dims):

        self.input_dims = input_dims
        self.output_dims = output_dims

        # inherit from nn module class
        super(PolicyNetwork, self).__init__()

        # initialize_network
        self.initialize_network()

        # define optimizer
        self.optimizer = torch.optim.Adam(lr=alpha, params=self.parameters())

        # define loss
        #self.loss = torch.nn.NLLLoss()

    def loss(self, actions, advantages):

        loss = -torch.log(actions)*(advantages)
        loss = torch.sum(loss)
        return loss

    # initialize network
    def initialize_network(self):

		# define network components
        self.fc1 = torch.nn.Linear(self.input_dims, 3)
        self.fc2 = torch.nn.Linear(3, 3)
        self.fc3 = torch.nn.Linear(3, self.output_dims)
        self.relu = torch.nn.ReLU()
        self.sigmoid = torch.nn.Sigmoid()
        self.tanh = torch.nn.Tanh()

    def forward(self, x):
        out = self.fc1(x)
        out = self.tanh(out)
        out = self.fc2(out)
        out = self.tanh(out)
        out = self.fc3(out)
        out = self.sigmoid(out)
        return out

    def update(self, actions, advantages, iter):

        for i in range(iter):

            # zero the parameter gradients
            self.optimizer.zero_grad()

            # calculate loss
            loss = self.loss(actions, advantages)

            # optimize
            loss.backward(retain_graph=True)
            self.optimizer.step()


def main():

    x = torch.ones(100, 2, requires_grad=True)
    y = torch.ones(100, 1, requires_grad=True)/10

    # define PolicyNetwork
    pn = PolicyNetwork(alpha=0.1, input_dims=2, output_dims=1)

    pn.update(x, y, 100)

if __name__ == "__main__":
    main()
