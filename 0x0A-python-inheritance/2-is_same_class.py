#!/usr/bin/python3
"""This module defines a function that checks if an object is exactly
    an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """Returns true if the object is exactly an instance of the specified
    class.
    """
    return type(obj) is a_class
