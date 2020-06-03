#!/usr/bin/python3
""" a simple script that create a json from input"""
import sys
import os.path as exist

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
"""creates an Object from a JSON file"""
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
"""writes an Object to a text file, using a JSON representation"""

"""dumps() — to serialize an object to a JSON formatted string."""
"""loads() — to deserialize a JSON document to a Python object."""

"""The list must be saved as a JSON representation in a file named
    add_item.json"""
if __name__ == '__main__':
    if len(sys.argv) == 1:
        if not exist.isfile('add_item.json'):
            save_to_json_file([], 'add_item.json')

    with open('add_item.json') as js:
        try:
            a = load_from_json_file('add_item.json')
        except Exception as e:
            save_to_json_file([], 'add_item.json')
            a = load_from_json_file('add_item.json')
        if type(a) is not list:
            save_to_json_file([], 'add_item.json')
            a = load_from_json_file('add_item.json')
        for arg in range(1, len(sys.argv)):
            a.append(sys.argv[arg])
            save_to_json_file(a, 'add_item.json')
