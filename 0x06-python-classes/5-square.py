#!/usr/bin/python3
"""This module defines a Square class"""


class Square:
    """Represents a square with a size that can be set and used to compute
       area
    """
    def __init__(self, size=0):
        """Initializes the square with a given size.

        Args:
            size(int): The size of the square.

        Raises:
          TypeError: If size is not an integer.
          ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter for size with validation"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates and returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints in the stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for k in range(self.__size):
                    print("#", end="")
                print()
