#!/usr/bin/env python3
"""
Write a function def np_elementwise(mat1, mat2)
that performs element-wise addition,
subtraction, multiplication, and division
"""


def np_elementwise(mat1, mat2):
    """
    Perform element-wise addition, subtraction, multiplication, and division.

    Args:
        mat1 (numpy.ndarray): The first input matrix.
        mat2 (numpy.ndarray): The second input matrix.

    Returns:
        tuple: A tuple containing the results of element-wise addition, 
               subtraction, multiplication, and division, in that order.
    """
    add = mat1 + mat2
    sub = mat1 - mat2
    mult = mat1 * mat2
    divide = mat1 / mat2
    return add, sub, mult, divide
