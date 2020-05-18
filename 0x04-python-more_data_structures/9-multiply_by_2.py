#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if not a_dictionary:
        return a_dictionary
    new_dict = a_dictionary.copy()
    for a_key in new_dict:
        new_dict[a_key] = new_dict[a_key] * 2
    return new_dict
#    new_dic = {doub: v * 2 for doub, v in a_dictionary.items()}
