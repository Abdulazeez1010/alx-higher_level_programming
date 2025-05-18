#!/usr/bin/python3
"""This module defines a function that writes an Object to a text file,
    using a JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """This function writes an Object to a text file, using a JSON
        representation.

    Args:
        my_obj: The Object to be written.
        filename: The text file.
    """
    with open(filename, 'w', encoding="utf") as f:
        json.dump(my_obj, f)
