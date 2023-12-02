#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest)"""
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2], sys.argv[1])
    request = requests.get(url)
    commits = request.json()
    try:
        for i in range(10):
            print(commits[i].get("sha"))
            print(commits[i].get("commit").get("author").get("name"))
    except IndexError:
        pass
