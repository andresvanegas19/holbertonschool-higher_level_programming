#!/usr/bin/python3
""" This script fetch information with the library urllib """


if __name__ == '__main__':
    import urllib.request
    import sys
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as r:
            print(r.read().decode())
    except urllib.error.HTTPError as exception:
        print("Error code: {:3.3}".format(
                exception.__str__().split()[2]))
