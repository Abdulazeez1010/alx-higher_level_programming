#!/usr/bin/python3
"""This module defines a function that prints a square"""


def print_square(size):
    """Prints a square.

    Args:
        size (int): size of the square.

    Raises:
        TypeError: If size is not an integer.
        TypeError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        print('#' * size)
