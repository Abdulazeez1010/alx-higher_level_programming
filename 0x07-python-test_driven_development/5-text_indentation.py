#!/usr/bin/python3
"""This module defines a function that prints 2 new lines after
    some delimeter.
"""


def text_indentation(text):
    """Prints 2 new lines after each of the characters:'.', '?', and ':'

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for i in range(len(text)):
        # My way: if text[i] == '.' or text[i] == '?' or text[i] == ':':
        if text[i] in '.?:':
            print(text[i], end="")
            print('\n')
            continue
        print(text[i], end="")
