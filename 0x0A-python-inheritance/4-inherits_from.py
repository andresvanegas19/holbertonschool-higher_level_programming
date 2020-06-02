#!/usr/bin/python3
"""Test if the object is inherent of a class"""


def inherits_from(obj, a_class):
    """function that validated if the object is
    a instace of a class in python"""
    try:
        return isinstance(obj, a_class)
    except TypeError:
        return False
