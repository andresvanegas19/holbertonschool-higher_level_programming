#!/usr/bin/python3
""" This script fetch information with the library urllib """


if __name__ == '__main__':
    import requests
    import sys
    headers = {
        'Authorization': 'token ' + '725a040c7aa0dc565ffd5e476cfde14131696520'}
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
