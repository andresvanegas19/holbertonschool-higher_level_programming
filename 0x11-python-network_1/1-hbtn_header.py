#!/usr/bin/python3
""" This script fetch information with the library urllib """


if __name__ == '__main__':
    import urllib.request
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url) as r:
        print(r.getheader('X-Request-Id'))
