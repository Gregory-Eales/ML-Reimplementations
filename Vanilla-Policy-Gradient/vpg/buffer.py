import torch


class Buffer(object):

    def __init__(self):

        # store actions
        self.action_buffer = []

        # store state
        self.observation_buffer = []

        # store reward
        self.reward_buffer = []
