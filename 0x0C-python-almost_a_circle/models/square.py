#!/usr/bin/python3
"""This module defines the Square class."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from Rectangle class."""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor."""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overrides the str method."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes.

        Args:
            *args: Assigns an argument to each attribute in the order:
            id, size, x, y.
            **kwargs: Assigns a key/value argument to attributes.

        Note:
            **kwargs is skipped if *args exists and is not empty.
        """
        if args and args is not None:
            attributes = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
