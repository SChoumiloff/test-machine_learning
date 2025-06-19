#!/usr/bin/env python3
"""
No neuron 3
"""
import numpy as np


class Neuron:
    """No neuron 3
    """
    def __init__(self, nx: int):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        self.nx = nx
        self._W = np.random.normal(size=(1, self.nx))
        self._b = 0
        self._A = 0

    def forward_prop(self, X):
        Z = np.matmul(self._W, X) + self._b
        self._A = 1 / (1 + np.exp(-Z))
        return self._A

    @property
    def W(self):
        return self._W

    @property
    def b(self):
        return self._b

    @property
    def A(self):
        return self._A
