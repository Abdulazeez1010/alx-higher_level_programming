#!/usr/bin/python3
"""This module defines a function that reads a file"""


def read_file(filename=""):
    """Reads a file."""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
