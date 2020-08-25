#!/usr/bin/python3
""" This script fetch information with the library urllib """


if __name__ == '__main__':
    import requests
    import sys
    url = sys.argv[1]
    try:
        r = requests.get(url)
        if r.status_code >= 400:
            r.raise_for_status()
        print(r.text)
    except requests.exceptions.RequestException as e:
        # raise SystemExit(err)
        print("Error code: {}".format(e.__str__().split()[0]))
