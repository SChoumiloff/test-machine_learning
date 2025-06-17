#!/usr/bin/env python3

def matrix_shape(matrix):
    dimensions = []
    while True:
        if isinstance(matrix, list) and len(matrix) > 0:
            dimensions.append(len(matrix))
            matrix = matrix[0]
        else:
            break
    return dimensions
