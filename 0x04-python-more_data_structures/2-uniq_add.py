#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    added = set()
    for num in my_list:
        if num not in added:
            sum += num
            added.add(num)
    return sum
