#!/usr/bin/python3
""" a simple script that handle a files"""

import json


def to_json_string(my_obj):
    """that returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
