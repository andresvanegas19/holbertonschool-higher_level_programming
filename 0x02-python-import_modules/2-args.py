#!/usr/bin/python3
import sys as s

if __name__ == "__main__":
    if (len(s.argv) is 1):
        print("0 arguments.")
    else:
        if (len(s.argv) is 2):
            print("{:d} argument:".format(len(s.argv) - 1))
            print("1: {}".format(s.argv[1]))
        else:
            print("{:d} arguments:".format(len(s.argv) - 1))
            for word, num in zip(s.argv, range(0, len(s.argv))):
                if (num is not 0):
                    print("{:d}: {}".format(num, word))
