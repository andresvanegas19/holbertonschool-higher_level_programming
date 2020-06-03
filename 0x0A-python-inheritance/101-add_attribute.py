#!/usr/bin/python3
"""simple script"""


def add_attribute(Class_v, class_att, fill_atr):
    """this functio track how many t"""
    if isinstance(Class_v, type):
        setattr(Class_v, class_att, fill_atr)
    else:
        raise Exception('can\'t add new attribute')


    # class_v.counter = getattr(class_v, "counter", 0) + 1
    # if getattr(class_v, "counter") > 1:
    # raise Exception('can\'t add new attribute')
