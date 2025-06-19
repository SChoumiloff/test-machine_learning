#!/usr/bin/env python3
"""
No neuron
"""
import numpy as np


class Neuron:
    """No Neuron
    """
    def __init__(self, nx: int):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise TypeError("nx must be a postive integer")
        self.nx = nx
        self.W = np.random.normal(size=(1, self.nx))
        self.b = 0
        self.A = 0
