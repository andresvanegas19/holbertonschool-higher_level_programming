#!/usr/bin/python3
"""Test if the object is inherent of a class"""


def is_same_class(obj, a_class):
    """function that validated if the object is
    a instace of a class in python"""
    try:
        return issubclass(a_class, type(obj))
    except TypeError:
        return False
