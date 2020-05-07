#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for a_key in a_dictionary:
        if a_key is key:
            del a_dictionary[a_key]
            return a_dictionary
    return a_dictionary
