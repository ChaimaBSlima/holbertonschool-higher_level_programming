#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list = []
    for div in range(0, len(my_list)):
        if my_list[div] % 2 == 0:
            list.append(True)
        else:
            list.append(False)
    return (list)
