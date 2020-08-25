#!/usr/bin/python3
""" This script fetch information with the library urllib """


if __name__ == '__main__':
    import requests
    import sys
    url = sys.argv[1]
    try:
        r = requests.post(url)
        print(r.raise_for_status())
    except requests.exceptions.RequestException as e:
        print("Error code: {}".format(e.__str__().split()[0]))
