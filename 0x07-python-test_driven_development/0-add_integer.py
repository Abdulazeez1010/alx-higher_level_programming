#!/usr/bin/python3
"""This module defines a function that adds two integers"""


def add_integer(a, b=98):
    if isinstance(a, bool) or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if isinstance(b, bool) or not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a)+int(b)
