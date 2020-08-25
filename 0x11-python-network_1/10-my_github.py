#!/usr/bin/python3
""" This script fetch information with the library urllib """


if __name__ == '__main__':
    import requests
    import sys
    token = sys.argv[2]
    headers = {'Authorization': 'token ' + token}
    login = requests.get('https://api.github.com/user', headers=headers)
    print(login.json().get('id'))
