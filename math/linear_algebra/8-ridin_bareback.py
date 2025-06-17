#!/usr/bin/env python3
"""
Module for matrix multiplication.
"""


def mat_mul(mat1, mat2):
    """
    Multiplies two matrices.

    Args:
        mat1 (list of list of floats/ints): The first matrix.
        mat2 (list of list of floats/ints): The second matrix.

    Returns:
        list of list of floats/ints: The resulting matrix
        after multiplication,
        or None if the matrices cannot be multiplied.
    """
    if mat1 is None or mat2 is None or len(mat1[0]) != len(mat2):
        return None

    res_mat = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            total = 0
            for k in range(len(mat2)):
                total += mat1[i][k] * mat2[k][j]
            row.append(total)
        res_mat.append(row)

    return res_mat
