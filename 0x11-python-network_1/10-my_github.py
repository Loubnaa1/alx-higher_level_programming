#!/usr/bin/python3
"""takes your GitHub credentials uses the GitHub API"""
import sys
import requests

if __name__ == "__main__":
    res = requests.get("https://api.github.com/user",
auth=(sys.argv[1], sys.argv[2]))
    print(res.json().get("id"))
