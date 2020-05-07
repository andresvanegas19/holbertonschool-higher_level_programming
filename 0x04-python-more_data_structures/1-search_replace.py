#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # (my_list, 2, 89)
    if not my_list:
        return my_list

    def search_number(num):
        if num is search:
            return replace
        else:
            return num
    new_list = list(map(search_number, my_list))

    return new_list
