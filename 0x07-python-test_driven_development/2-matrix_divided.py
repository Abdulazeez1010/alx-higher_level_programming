#!/usr/bin/python3
"""This module defines a function that divides all element of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div and returns a new matrix

    Args:
        matrix(list of lists): The amtrix to be divide.
        div(int or float): The divisor.

    Raises:
        TypeError: If matrix is not a list" of lists of integers/floats.
        TypeError: if rows of the matrix are not of the same size.
        TypeError: If div is not an int or a float.
        ZeroDivisionError: If div is zero.

    Returns:
        A new matrix with each value divided by div and rounded to 2 decimal
        places.
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(
            isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    try:
        return [[round(num/div, 2) for num in row] for row in matrix]
    except OverflowError:
        raise OverflowError("integer value too large")
