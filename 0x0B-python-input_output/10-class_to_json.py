#!/usr/bin/python3
""" a simple script that create a json from input"""


def class_to_json(obj):
    """for JSON serialization of an object
    :return  the dictionary description with simple data structure"""
    a = obj.__dict__
    return a
