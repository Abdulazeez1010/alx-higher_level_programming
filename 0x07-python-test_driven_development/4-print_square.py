#!/usr/bin/python3
"""This module defines """


def print_square(size):
    """Prints a square

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        print('#' * size)
