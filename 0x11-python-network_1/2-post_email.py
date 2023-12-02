#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request , and displays the body"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    value = {"email": sys.argv[2]}
    donne = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(sys.argv[1], donne)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
