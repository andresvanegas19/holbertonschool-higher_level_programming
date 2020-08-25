#!/usr/bin/python3
""" This script fetch information with the library urllib """


if __name__ == '__main__':
    encode = [57, 52, 97, 51, 51, 101,
              53, 48, 52, 51, 53, 48, 51, 53, 102,
              48, 54, 52, 51, 55, 51, 51, 54, 55, 49,
              99, 55, 55, 49, 54, 54, 97, 52, 52, 57,
              48, 100, 51, 102, 55]
    import requests
    import sys
    headers = {
        'Authorization': 'token ' + "".join(chr(p) for p in encode)}
    # /{owner}/{repo}/commits
    login = requests.get(
        'https://api.github.com/repos/{}/{}/commits'.format(
                sys.argv[1], sys.argv[2]), headers=headers)

    for commit in range(10):
        information = login.json()[commit]
        print("{}: {}".format(
            information.get('sha'),
            information.get('commit').get("author").get("name")
        ))
