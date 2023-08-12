#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    length = len(dir(hidden_4))
    for i in range(0, length):
        if dir(hidden_4)[i][0] == "_":
            continue
        print(dir(hidden_4)[i])
