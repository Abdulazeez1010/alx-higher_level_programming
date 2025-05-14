#!/usr/bin/python3
"""This module defines a Square class that inherits from a Rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle class"""
    def __init__(self, size):
        """Initializes the class Square with a size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the Square"""
        return self.__size ** 2

    def __str__(self):
        """Returns the Square description"""
        return '[Square] {}/{}'.format(self.__size, self.__size)
