#!/usr/bin/python3
"""lists the 10 most recent commits on a given Github repo
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    req = requests.get(url)
    com = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                com[i].get("sha")
                com[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
