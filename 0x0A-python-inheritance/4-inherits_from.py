#!/usr/bin/python3
"""Test if the object is inherent of a class"""


def inherits_from(obj, a_class):
    """function that validated if the object is
    a instace of a class in python"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False