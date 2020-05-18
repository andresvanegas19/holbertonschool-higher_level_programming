#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    total = 0
    for num in range(x):
        if num < x:
            try:
                print("{}".format(my_list[num]), end='')
                total += 1
            except IndexError:
                print()
                return total - 1
    print()
    return total
