#!/usr/bin/python3
def uppercase(str):
    for i in str:
        for j in range(97, 123):
            if ord(i) == j:
                i = chr(j - 32)
        print("{}".format(i), end="")
    print()
