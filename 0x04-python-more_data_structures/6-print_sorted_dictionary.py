#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_list = sorted(a_dictionary)
    for element in sorted_list:
        print("{}: {}".format(element, a_dictionary[element]))
