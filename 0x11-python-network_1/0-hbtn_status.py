#!/usr/bin/python3
""" This script fetch information with the library urllib """

if __name__ == '__main__':
    import urllib.request
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as r:
        print("Body response:")
        response = r.read()
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode()))
