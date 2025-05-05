#!/usr/bin/python3
"""This module defines an empty class Rectangle"""


class Rectangle:
    """Rectangle class

    Args:
        width (int): width of the rectangle
        height (int): height of the rectangle

    Raises:
        TypeError: If width or height is not an integer
        ValueError: If width or height is less than 0
    """
    def __init__(self, width=0, height=0):
        """Initializes the rectangle with a given size"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for with"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Calculates and return the area of the rectangle"""
        return self.__width*self.__height

    def perimeter(self):
        """Calculates and return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width+self.__height)

    def __str__(self):
        """Prints the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        for i in range(self.__height):
            if i == self.__height-1:
                result += "#"*self.__width
                continue
            result += "#"*self.__width + "\n"
        return result

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)
