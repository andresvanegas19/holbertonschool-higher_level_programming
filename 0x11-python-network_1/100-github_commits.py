#!/usr/bin/python3
""" This script fetch information with the library urllib """


if __name__ == '__main__':
    import requests
    import sys
    headers = {'Authorization': 'token 6acbd46823412b121b92e54589e78d0122d4209f'}
    # /{owner}/{repo}/commits
    login = requests.get(
        'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[1], sys.argv[2]),
        headers=headers)

    for commit in range(10):
        information = login.json()[commit]
        print("{}: {}".format(
            information.get('sha'),
            information.get('commit').get("author").get("name")
        ))

