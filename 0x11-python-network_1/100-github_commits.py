#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest)"""
from sys import argv
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    request = requests.get(url)
    commits = request.json()
    try:
        for i in range(10):
            print(commits[i].get("sha"), end=': ')
            print(commits[i].get("commit").get("author").get("name"))
    except IndexError:
        pass
