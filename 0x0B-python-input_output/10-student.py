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

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            diction = {}
            for attr in attrs:
                if attr in self.__dict__:
                    diction[attr] = self.__dict__[attr]
            return diction
        return self.__dict__
