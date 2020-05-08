#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for a_key in list(a_dictionary):
        if a_dictionary[a_key] is value:
            del a_dictionary[a_key]
    return a_dictionary
