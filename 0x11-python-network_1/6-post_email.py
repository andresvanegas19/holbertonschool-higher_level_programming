#!/usr/bin/python3
""" This script fetch information with the library urllib """


if __name__ == '__main__':
    import requests
    import sys
    url = sys.argv[1]
    r = requests.post(url, data={'email': sys.argv[2]})
    print(r.text)
