#!/usr/bin/python3
"""This module defines a Student class."""


class Student:
    """A student class."""
    first_name = ""
    last_name = ""
    age = ""

    def __init__(self, first_name, last_name, age):
        """Initializes the class with a first_name, last_name, and an age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance."""
        return self.__dict__
