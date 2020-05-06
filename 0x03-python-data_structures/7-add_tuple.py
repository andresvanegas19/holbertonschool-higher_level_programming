#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    try:
        tupa1 = tuple_a[0]
    except:
        tupa1 = 0
    try:
        tupb1 = tuple_b[0]
    except:
        tupb1 = 0

    try:
        tupa2 = tuple_a[1]
    except:
        tupa2 = 0
    try:
        tupb2 = tuple_b[1]
    except:
        tupb2 = 0

    return ((tupa1 + tupb1, tupa2 + tupb2))
