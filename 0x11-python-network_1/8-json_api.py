#!/usr/bin/python3
"""Script that takes in a letter
sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    pl = {"q": letter}
    req = requests.post("http://0.0.0.0:5000/search_user", data=pl)
    try:
        res = req.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
