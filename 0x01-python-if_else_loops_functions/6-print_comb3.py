#!/usr/bin/python3
for i in range(48, 58):
    j = i + 1
    while j < 58:
        if i == 56 and j == 57:
            print("{}{}".format(chr(i), chr(j)))
            break
        print("{}".format(chr(i)), end="")
        print("{}, ".format(chr(j)), end="")
        j = j + 1
