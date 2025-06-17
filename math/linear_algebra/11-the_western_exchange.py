#!/usr/bin/env python3

"""
Module transpose np
"""
import numpy as np


def np_transpose(matrix):
    """
    Transpose a given matrix using NumPy.

    Parameters:
        matrix (numpy.ndarray): The input matrix to be transposed.

    Returns:
        numpy.ndarray: The transposed matrix.
    """
    a = np.transpose(matrix)
    return a
