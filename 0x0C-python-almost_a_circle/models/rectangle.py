#!/usr/bin/python3
"""This module defines a class Rectangle that inherits from the Base class"""


class Rectangle(Base):
    """Inherits from the Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
