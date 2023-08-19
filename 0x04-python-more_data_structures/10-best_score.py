#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    largest_key = next(iter(a_dictionary))
    largest_value = a_dictionary[largest_key]
    for key in a_dictionary:
        if a_dictionary[key] > largest_value:
            largest_key = key
    return largest_key
