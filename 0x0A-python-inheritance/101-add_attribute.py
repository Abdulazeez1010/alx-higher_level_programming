#!/usr/bin/python3
"""This module defines a function that adds a new attribute"""


def add_attribute(obj, attr_name, value):
    """Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to which an attribute is to be added.
        attr_name: The name of the attribute.
        value: The value to assign to the attribute.

    Raises:
        TypeError: If new attribute can't be added.
    """

    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, value)
    else:
        raise TypeError("can't add new attribute")
