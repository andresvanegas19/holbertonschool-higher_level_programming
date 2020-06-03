#!/usr/bin/python3
""" a simple script that handle a JSONS"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, 'a', encoding='utf-8') as fl:
        fl.write(json.dumps(my_obj))

