#!/usr/bin/python3
"""takes your GitHub credentials uses the GitHub API"""
from sys import argv
import requests

if __name__ == "__main__":
    res = requests.get("https://api.github.com/user", iauth=(argv[1], argv[2]))
    print(res.json().get("id"))
