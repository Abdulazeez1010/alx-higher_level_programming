#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = []
    for x in range(len(my_list)i):
        new_list.append(my_list[x])
    new_list[idx] = element
    return new_list
