#!/usr/bin/python3
def no_c(my_string):
    string = [word for word in my_string if word not in 'Cc']
    strin = ""
    return (strin.join(string))
