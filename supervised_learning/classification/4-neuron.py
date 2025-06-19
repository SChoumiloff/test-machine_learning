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
        self.__W = np.random.normal(size=(1, self.nx))
        self.__b = 0
        self.__A = 0

    def forward_prop(self, X):
        """forward prop documentation
        """
        Z = np.matmul(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-Z))
        return self.__A

    def cost(self, Y, A):
        """Compute
        """
        m: int = Y.shape[1]
        coef = - 1 / m
        assert Y.shape[1] == A.shape[1]
        cost = coef * np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))
        return cost

    def evaluate(self, X, Y):
        """evaluate the models
        """
        A = self.forward_prop(X)
        cost = self.cost(Y, A)
        predictions = np.where(A >= 0.5, 1, 0)
        return predictions, cost

    @property
    def W(self):
        return self.__W

    @property
    def b(self):
        return self.__b

    @property
    def A(self):
        return self.__A
