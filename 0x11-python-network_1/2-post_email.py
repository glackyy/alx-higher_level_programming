#!/usr/bin/python3
"""Script that sends a POST request to the
passed URL, takes the email as a parameter
displays the body of the response
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(val).encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
