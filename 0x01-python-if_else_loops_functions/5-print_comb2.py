#!/usr/bin/python3
for number in range(0,100):
    if (number is not 99):
        if (number < 10):
            print("0{}".format(number),end=", ")
        else:
            print("{}".format(number),end=", ")
    else:
        print("99")
