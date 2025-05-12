#!/usr/bin/python3
"""This module defines a class MyList that inherits from list"""


class MyList(list):
    def print_sorted(self):
        """Prints the list sorted (ascending sort)"""
        print(sorted(self))
