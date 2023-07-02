#!/usr/bin/python3

"""Defining matrix divided"""


def matrix_divided(matrix, div):
    """Divivdes all elements of a matrix

    Args:
        matrix: (list)
        div: (int or float)

    Returns:
           list
    """
    if not isinstance(matrix, list) 
        and all(isinstance(e, (int, float)) for e in row)
        for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integer/floats")

    if not matrix or not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    n_matrix = []
    for row in matrix:
        n_row = [round(e /div, 2) for e in row]
        n_matrix.append(n_row)

    return n_matrix
