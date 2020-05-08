#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = 0
    didi = 0
    for (x, y) in my_list:
        total += y
        didi += x * y

    return didi / total
