#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    for i in range(len(my_string)):
        if my_string[i] == chr(99) or my_string[i] == chr(67):
            continue
        new_string += my_string[i]
    return new_string
