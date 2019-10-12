import torch

class ValueNetwork(torch.nn.Module):

    def __init__(self, alpha, input_dims, output_dims):

        self.input_dims = input_dims
        self.output_dims = output_dims

        # inherit from nn module class
        super(ValueNetwork, self).__init__()

        # initialize_network
        self.initialize_network()

        # define optimizer
        self.optimizer = torch.optim.Adam(lr=alpha, params=self.parameters())

        # define loss
        self.loss = torch.nn.MSELoss()

        # get device
        self.device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu:0')
        self.to(self.device)


    # initialize network
    def initialize_network(self):

		# define network components
        self.fc1 = torch.nn.Linear(self.input_dims, 5)
        self.fc2 = torch.nn.Linear(5, 5)
        self.fc3 = torch.nn.Linear(5, self.output_dims)
        self.relu = torch.nn.ReLU()
        self.sigmoid = torch.nn.Sigmoid()
        self.tanh = torch.nn.Tanh()

    def forward(self, x):
        x = torch.Tensor(x).to(self.device)
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc3(out)
        out = self.sigmoid(out)
        return out.to(torch.device('cpu:0'))

    def update(self, observations, rewards, iter):

        observations = torch.Tensor(observations).to(self.device)
        rewards = torch.Tensor(rewards).to(self.device)

        for i in range(iter):

            # zero the parameter gradients
            self.optimizer.zero_grad()

            # make prediction
            prediction = self.forward(observations)

            # calculate loss
            loss = self.loss(prediction, rewards)

            # optimize
            loss.backward(retain_graph=True)
            self.optimizer.step()


def main():

    x = torch.ones(100, 2)
    y = torch.ones(100, 2)

    # defin value ValueNetwork
    vn = ValueNetwork(alpha=0.01, input_dims=2, output_dims=2)

    vn.update(x, y, 100)

if __name__ == "__main__":
    main()
