#!/usr/bin/env python3
"""
Module for concatenating two 2D matrices along a specified axis.
"""

def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two 2D matrices along a specified axis.

    Args:
        mat1 (list of lists): The first 2D matrix.
        mat2 (list of lists): The second 2D matrix.
        axis (int): The axis along which to concatenate (0 for rows, 1 for columns).

    Returns:
        list of lists: The concatenated matrix, or None if the axis is invalid.
    """
    if len(mat1) != len(mat2):
        return None
    matrix = []
    if axis == 0:
        for i in range(len(mat1)):
            matrix.append(mat1[i])
        for i in range(len(mat2)):
            matrix.append(mat2[i])
        return matrix
    elif axis == 1:
        matrix = [row[:] for row in mat1]
        for i in range(len(mat2)):
            for j in range(len(mat2[i])):
                matrix[i].append(mat2[i][j])
        return matrix
    else:
        return None
