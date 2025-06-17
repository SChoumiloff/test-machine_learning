#!/usr/bin/env python3

def matrix_transpose(matrix):
    """Transpose a given matrix.
    This function takes a 2D list (matrix) as input and returns its transpose.
    The transpose of a matrix is obtained by flipping rows and columns.
    Args:
        matrix (list): A 2D list representing the matrix to be transposed.
    Returns:
        list: A 2D list representing the transposed matrix.
    Raises:
        SystemExit: If the input is not a list, the program exits.
    Example:
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> matrix_transpose(matrix)
        [[1, 4], [2, 5], [3, 6]]
    """

    if not isinstance(matrix, list):
        exit(0)
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
