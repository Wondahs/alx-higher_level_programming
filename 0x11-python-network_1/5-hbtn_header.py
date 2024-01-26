#!/usr/bin/python3
''' fetches https://alx-intranet.hbtn.io/status using requests'''


if __name__ == '__main__':
    import requests
    url = 'https://alx-intranet.hbtn.io/status'
    content = requests.get(url)
    request_id = content.headers.get('X-Request-Id')
    print(request_id)
