#!/usr/bin/python3
"""
Containing a function that devides all
elements of a matrix
"""

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    numb_rows = len(matrix)
    numb_cols = len(matrix[0])

    if not all(len(row) == numb_cols for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix

