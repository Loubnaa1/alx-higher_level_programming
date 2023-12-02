#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the valu.
"""
import sys
import requests


if __name__ == "__main__":
    responce = requests.get(sys.argv[1])
    print(responce.headers.get("X-Request-Id"))
