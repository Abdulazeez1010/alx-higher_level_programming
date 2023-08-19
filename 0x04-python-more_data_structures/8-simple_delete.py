#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary:
        return a_dictionary
    new_dictionary = a_dictionary
    del new_dictionary[key]
    return new_dictionary
