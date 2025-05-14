#!/usr/bin/python3
"""This module defines an empty class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class with basic geometry validation methods"""
    pass

    def area(self):
        """Raises an Exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates that value is a positive integer.

        Args:
            name(str): Name of the value.
            value(int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value < 0 or value == 0:
            raise ValueError('{} must be greater than 0'.format(name))
