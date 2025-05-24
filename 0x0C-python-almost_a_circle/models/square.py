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
        """Overrrides the str method."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)
