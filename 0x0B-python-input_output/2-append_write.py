#!/usr/bin/python3
"""This modules defines a function that appends a string at the end
    of a text file.
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file and returns the
        number of characters added.

    Args:
        filename: The name of the file.
        text: The string to append.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
    return len(text)
