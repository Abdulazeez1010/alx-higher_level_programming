#!/usr/bin/python3
"""This modules defines a rebel class that inherits from int"""


class MyInt(int):
    """Inherits from int.
    This class is a rebel. It has == and != operators inverted.
    """
    def __eq__(self, other):
        """Overrides the == operator to perform != instead."""
        return int(self) != other

    def __ne__(self, other):
        """Overrides the != operator to perform == instead."""
        return int(self) == other
