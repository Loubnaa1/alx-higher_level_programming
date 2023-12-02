#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response."""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    value = {"email": sys.argv[2]}
    donne = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(sys.argv[1], donne)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
