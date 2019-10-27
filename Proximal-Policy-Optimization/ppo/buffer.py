import torch
import numpy as np

class Buffer(object):

    def __init__(self):

        # store actions
        self.action_buffer = []

        # store state
        self.observation_buffer = []

        # store reward
        self.reward_buffer = []

        # store advantage
        self.advantage_buffer = []

        # store log prob
        self.log_probs = []

        # params
        self.params = None

    def store_observation(self, obs):
        self.observation_buffer.append(obs)

    def store_reward(self, rwrd):
        self.reward_buffer.append(rwrd)

    def store_action(self, act):
        self.action_buffer.append(act)

    def store_advantage(self, adv):
        self.advantage_buffer.append(adv)

    def store_parameters(self, params):
        self.params = params

    def store_log_prob(self, log_prob):
        self.log_probs.append(log_prob)

    def get_log_probs(self):
        return torch.Tensor(self.log_probs)

    def get_observations(self):
        return torch.Tensor(self.observation_buffer[1:])

    def get_rewards(self):
        return torch.Tensor(self.reward_buffer).reshape(-1, 1)

    def get_actions(self):
        return torch.cat(self.action_buffer)

    def get_advantages(self):
        return torch.Tensor(self.advantage_buffer)

    def clear_buffer(self):
        # store actions
        self.action_buffer = []

        # store state
        self.observation_buffer = []

        # store reward
        self.reward_buffer = []

        # store advantage
        self.advantage_buffer = []

    def get_tensors(self):

        observations = torch.Tensor(self.observation_buffer[1:])
        actions = torch.cat(self.action_buffer)
        rewards = torch.Tensor(self.reward_buffer).reshape(-1, 1)
        advantages = torch.Tensor(self.advantage_buffer)

        return observations, actions, rewards, advantages