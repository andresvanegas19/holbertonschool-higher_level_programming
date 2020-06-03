#!/usr/bin/python3
""" a simple script that handle a JSONS"""

import json

"""The difference is that
    .load() parses a file object
    .loads() parses a string / unicode object."""


def from_json_string(my_str):
    """ function that returns an object (Python data structure)
    represented by a JSON string:"""
    return json.loads(my_str)
