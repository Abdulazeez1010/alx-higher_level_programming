#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            res = my_list_1[i]/my_list_2[i]
            result.append(res)
        except (ZeroDivisionError):
            res = 0
            result.append(res)
            print("division by 0")
        except (TypeError):
            res = 0
            result.append(res)
            print("wrong type")
        except IndexError:
            res = 0
            result.append(res)
            print("out of range")
    return result
