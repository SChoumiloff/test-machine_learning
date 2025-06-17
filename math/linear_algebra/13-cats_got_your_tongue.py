#!/usr/bin/env python3
"""
concatenates two matrices along a specific axis
"""


def np_cat(mat1, mat2, axis=0):
    """
    Concatenate two numpy arrays along a specified axis.

    Parameters:
    mat1 (numpy.ndarray): The first array to concatenate.
    mat2 (numpy.ndarray): The second array to concatenate.
    axis (int, optional): The axis along which the arrays
    will be concatenated.
    
    Default is 0.

    Returns:
    numpy.ndarray: The concatenated array.

    Example:
    >>> import numpy as np
    >>> mat1 = np.array([[1, 2], [3, 4]])
    >>> mat2 = np.array([[5, 6]])
    >>> np_cat(mat1, mat2, axis=0)
    array([[1, 2],
           [3, 4],
           [5, 6]])
    """
    import numpy as np
    return np.concatenate((mat1, mat2), axis=axis)
