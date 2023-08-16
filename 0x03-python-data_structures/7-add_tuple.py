#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    length_a = len(tuple_a)
    length_b = len(tuple_b)
    if length_a < 2:
        for i in range(2 - length_a):
            tuple_a = tuple_a + (0,)
    if length_b < 2:
        for i in range(2 - length_b):
            tuple_b = tuple_b + (0,)
    if length_a > 2:
        tuple_a = tuple_a[:2]
    if length_b > 2:
        tuple_b = tuple_b[:2]
    return tuple(a + b for a, b in zip(tuple_a, tuple_b))
