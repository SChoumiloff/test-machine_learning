#!/usr/bin/env python3
"""
this module compute shape of nparray
"""


import numpy as np


def np_shape(matrix: np.ndarray) -> tuple:
    """
    Get the shape of a numpy array.

    Args:
        matrix (np.ndarray): The input numpy array.

    Returns:
        tuple: The shape of the numpy array.
    """
    return matrix.shape