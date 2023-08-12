#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    add_val = add(a, b)
    sub_val = sub(a, b)
    mul_val = mul(a, b)
    div_val = div(a, b)
    print("{} + {} = {}".format(a, b, add_val))
    print("{} - {} = {}".format(a, b, sub_val))
    print("{} * {} = {}".format(a, b, mul_val))
    print("{} / {} = {}".format(a, b, div_val))
