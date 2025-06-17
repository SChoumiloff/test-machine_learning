#!/usr/bin/env python3
"""
module for matrix shape
"""


def matrix_shape(matrix):
    """The function determines the dimensions of
    a nested list (matrix) by iteratively
    traversing its structure and counting
    the number of elements at each level.

    Args:
        matrix (list): A nested list representing
        the matrix.

    Returns:
        list: A list of integers representing the dimensions
        of the matrix. For example, a 2x3 matrix will return
        [2, 3].
    """
    dimensions = []
    while True:
        if isinstance(matrix, list) and len(matrix) > 0:
            dimensions.append(len(matrix))
            matrix = matrix[0]
        else:
            break
    return dimensions
