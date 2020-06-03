#!/usr/bin/python3
""" a simple script that handle a files"""

import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”
    :return a object"""
    with open(filename, 'r', encoding='utf-8') as fl:
        """creates an Object from a JSON file"""
        return json.loads(fl.read())
