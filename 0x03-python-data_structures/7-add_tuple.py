#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    numa_one = numa_two = numb_one = numb_two = 0
    if (len(tuple_a) >= 2):
        numa_one, numa_two = tuple_a
    if (len(tuple_b) >= 2):
        numb_one, numb_two = tuple_b

    print(str(numa_one) + " " + str(numb_one))
    print(str(numa_two) + " " + str(numb_two))
    new_tuple = (numa_one + numb_one, numa_two + numb_two)
    return (new_tuple)

tuple_a = (.)
tuple_b = (88, 11)

try:
    a = tuple_a[0]
except:
    a =  0