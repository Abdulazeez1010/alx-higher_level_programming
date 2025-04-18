#!/usr/bin/python3
"""This module defines a Square class"""


class Square:
    """This class defines a square"""
    def __init__(self, size=0):
        """Initializes the square with a given size.

        Args:
            size(int): The size of the square (must be >= 0).

        Raises:
            TypeError: If size is not an integer.
            valueError: If size < 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        return self.__size ** 2
