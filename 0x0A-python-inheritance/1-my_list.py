#!/usr/bin/python3
"""This module defines a class MyList that inherits from list"""


class MyList(list):
    """A custom list class that adds a method to print the list in sorted
    order.

    Inherits from:
        list: The built-in list class.
    """

    def print_sorted(self):
        """Returns a new containing the sorted elements"""
        print(sorted(self))
