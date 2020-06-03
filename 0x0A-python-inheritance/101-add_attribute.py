#!/usr/bin/python3
"""simple script"""


def add_attribute(class_v, class_att, fill_atr):
    """this functio track how many t"""
    if not isinstance(class_v, type(object)):
        raise Exception('can\'t add new attribute')
    if type(class_att) is not str:
        raise Exception('can\'t add new attribute')
    setattr(class_v, class_att, fill_atr)
    # class_v.counter = getattr(class_v, "counter", 0) + 1
    # if getattr(class_v, "counter") > 1:
    # raise Exception('can\'t add new attribute')
