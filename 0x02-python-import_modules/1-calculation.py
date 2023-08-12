#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
add_val = add(a, b)
sub_val = sub(a, b)
mul_val = mul(a, b)
div_val = div(a, b)
print(f"{a} + {b} = {add_val}")
print(f"{a} - {b} = {sub_val}")
print(f"{a} * {b} = {mul_val}")
print(f"{a} / {b} = {div_val}")
