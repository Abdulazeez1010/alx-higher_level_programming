#!/usr/bin/python3
"""This module defines a function that creates an Object
    from a “JSON file”.
"""


import json


def load_from_json_file(filename):
    """This function creates an Object from a “JSON file”.

    Args:
        filename: The JSON file.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
