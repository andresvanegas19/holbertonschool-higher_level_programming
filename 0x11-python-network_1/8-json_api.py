#!/usr/bin/python3
""" This script fetch information with the library urllib """


if __name__ == '__main__':
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        search = sys.argv[1]
    else:
        search = ""
    try:
        r = requests.post(url, data={'q': search})
        if r.status_code >= 400:
            r.raise_for_status()
        result = r.json()
        if not isinstance(result, dict):
            print("Not a valid JSON")
        elif not result:
            print("No result")
        elif type(result) == dict and result:
            # [<id>] <name>
            print("[{}] {}".format(
                result.get('id'),
                result.get('name')))
        else:
            pass

    except requests.exceptions.RequestException as e:
        print("Error code: {}".format(e.__str__().split()[0]))
