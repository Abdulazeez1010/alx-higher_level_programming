#!/usr/bin/python3
"""This module defines a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of
    characters written.

    args:
        filename: The name of the text file.
        text: The string to be written.

    Return: The number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    return len(text)
