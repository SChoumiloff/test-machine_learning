#!/usr/bin/env python3
"""
No neuron 2
"""
import numpy as np


class Neuron:
    """No neuron 2
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

    @property
    def W(self):
        return self._W

    @property
    def b(self):
        return self._b

    @property
    def A(self):
        return self._A

    @A.setter
    def A(self, a):
        self._A = a
