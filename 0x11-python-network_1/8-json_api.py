#!/usr/bin/python3
''' fetches https://alx-intranet.hbtn.io/status using requests'''


if __name__ == '__main__':
    import requests
    from sys import argv
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': argv[1] if argv[1] else ''}
    content = requests.post(url, data=data)
    try:
        json_data = content.json()
        if json_data == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
    except ValueError:
        print("Not a valid JSON")
