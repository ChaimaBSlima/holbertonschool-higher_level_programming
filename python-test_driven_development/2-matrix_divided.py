#!/usr/bin/python3

"""
This script defines a function 'matrix_divided' that divides
all elements of a matrix by a specified divisor.
"""


def matrix_divided(matrix, div):

    """
    Divides all elements of a matrix by the specified divisor.

    Parameters:
    - matrix (list of lists): The matrix to be divided.
    - div (int or float): The divisor.

    Returns:
    - new_matrix (list of lists): The resulting matrix after division.
    """

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(isinstance(elem, (int, float))
               for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list\
 of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix
