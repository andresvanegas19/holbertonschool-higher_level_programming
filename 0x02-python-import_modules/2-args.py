#!/usr/bin/python3
import sys as s

if __name__ == "__main__":
    if (len(s.argv) is 1):
        print("0 arguments.")
    else:
        print("{:d} argument:".format(len(s.argv)))
        for word, num in zip(s.argv, range(0,len(s.argv))):
            if (num is not 0):
                print("{:d}: {}".format(num, word))