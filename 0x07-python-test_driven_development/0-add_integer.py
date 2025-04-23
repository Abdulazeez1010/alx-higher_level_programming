#!/usr/bin/python3
"""This module defines a function that adds two integers"""


def add_integer(a, b=98):
    """Returns the sum of two integer.

    Args:
        a(int or float): The first number.
        b(int or float): The second number.

    Raises:
        TypeError: If a or b  are not int or float.
        OverflowError: If integer value is too large.

    Returns:
        int: The sum of a and b as an integer.
    """
    if isinstance(a, bool) or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if isinstance(b, bool) or not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    try:
        return int(a)+int(b)
    except OverflowError:
        raise OverflowError("integer value too large")
