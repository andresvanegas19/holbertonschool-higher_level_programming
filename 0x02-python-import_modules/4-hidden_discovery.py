#!/usr/bin/python3
import hidden_4 as hid

for function in dir(hid):
    if function[1] is not '_' and function[-1] is not '_':
        print(function)
