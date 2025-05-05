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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with a given size"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol = self.print_symbol

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
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
        self.print_symbol = str(self.print_symbol)
        for i in range(self.__height):
            if i == self.__height-1:
                result += self.print_symbol*self.__width
                continue
            result += self.print_symbol*self.__width + '\n'
        return result

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area.

        rect_1: First rectangle.
        rect_2: Second rectangle.

        Raises:
            TypeError if rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        area_1 = Rectangle.area(rect_1)
        area_2 = Rectangle.area(rect_2)
        if area_1 == area_2 or area_1 > area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
