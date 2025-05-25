#!/usr/bin/python3
"""This module defines a class Rectangle that inherits from the Base class"""


from models.base import Base


class Rectangle(Base):
    """Inherits from the Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for width"""
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for height"""
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for x"""
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for y"""
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        if self.y:
            for i in range(self.y):
                print()
        for i in range(self.__height):
            print(' '*self.x + '#'*self.__width)

    def __str__(self):
        """Overrides the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates the attributes of the Rectangle instance.

        Args:
            *args: Assigns an argument to each attribute in the order:
            id, width, height, x, y.
            **kwargs: Assigns a key/value argument to attributes.

        Note:
            **kwargs is skipped if *args exists and is not empty.
        """
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args and args is not None:
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
