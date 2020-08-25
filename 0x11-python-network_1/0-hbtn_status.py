#!/usr/bin/python3
""" This script fetch information with the library urllib """

if __name__ == '__main__':
    import urllib.request
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as r:
        print("Body response:")
        response = r.read()
        print("    - type: {}".format(type(response)))
        print("    - content: {}".format(response))
        print("    - utf8 content: {}".format(response.decode()))
