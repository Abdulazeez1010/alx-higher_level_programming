#!/usr/bin/python3
"""This module defines a function that inserts a line of text to a file,
    after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing a specific
        string.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        lines = f.readlines()

    new_content = []
    for line in lines:
        new_content.append(line)
        if search_string in line:
            new_content.append(new_string)

    with open(filename, 'w', encoding="utf-8") as f:
        f.writelines(new_content)
