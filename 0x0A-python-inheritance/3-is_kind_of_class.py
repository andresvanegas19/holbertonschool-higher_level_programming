#!/usr/bin/python3
"""Test if the object is inherent of a class"""


def is_kind_of_class(obj, a_class):
    """function that validated if the object is
    a instace of a class in python"""
    try:
        return isinstance(obj, a_class)
    except TypeError:
        return False
