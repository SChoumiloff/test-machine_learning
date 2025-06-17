#!/usr/bin/env python3
"""
Module for 2D matrix addition.
"""


def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise.

    Args:
        mat1 (list of lists): First matrix.
        mat2 (list of lists): Second matrix.

    Returns:
        list of lists: Resulting matrix after addition.
        None: If matrices have different dimensions.
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))]
            for i in range(len(mat1))]
