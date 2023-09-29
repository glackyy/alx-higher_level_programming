#!/usr/bin/python3
"""Script that takes in a URL
sends a request to the URL
displays the body of the response (utf-8)
"""
import sys
from urllib import request, error

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except error.HTTPError as err:
        print('Error code:', err.code)
