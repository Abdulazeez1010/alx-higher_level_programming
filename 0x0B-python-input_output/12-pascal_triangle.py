#!/usr/bin/python3
"""This module defines a function that returns integers representing
    a Pascal’s triangle.
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s
        triangle of n.
    """
    if n <= 0:
        return [[]]
    if n == 1:
        return [[1]]
    if n == 2:
        pasc = []
        pasc.append([1])
        pasc.append([1, 1])
        return pasc
    if n > 2:
        final_L = []
        final_L.append([1])
        last_L = [1, 1]
        final_L.append(last_L)
        for i in range(n - 2):
            new_L = []
            new_L.append(1)
            for i in range(len(last_L) - 1):
                new_L.append(last_L[i] + last_L[i + 1])
            new_L.append(1)
            last_L = new_L
            final_L.append(new_L)
        return final_L
