#!/usr/bin/python3
"""This module defines a Square class"""


class Square:
    """Represents a square with a size that can be set and used to compute
       area
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with a given size.

        Args:
            size(int): The size of the square.
            position: The positon (tuple of 2 positive integers).

        Raises:
          TypeError: If size is not an integer.
          ValueError: If size is less than 0.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the current area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints in the stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for h in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
