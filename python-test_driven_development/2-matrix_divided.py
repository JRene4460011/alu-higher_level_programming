#!/usr/bin/python3
"""Module that contains a function to divide a matrix by a number."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div and rounds to 2 decimals.

    Args:
        matrix (list of lists): matrix of integers/floats
        div (int or float): number to divide by

    Raises:
        TypeError: If matrix is not a list of lists of int/float
        TypeError: If rows are not the same size
        TypeError: If div is not a number
        ZeroDivisionError: If div is 0

    Returns:
        list: new matrix with divided values
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not all(
        all(isinstance(ele, (int, float)) for ele in row) for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_matrix.append([round(ele / div, 2) for ele in row])
    return new_matrix
