#!/usr/bin/python3
"""This module defines an empty class BaseGeometry"""


class BaseGeometry:
    """Empty class BaseGeometry"""
    pass

    def area(self):
        """Raises an Exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates value.

        name is always a string.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError('<name> must be an integer')
        if value < 0 or value == 0:
            raise ValueError('<name> must be greater than 0')
