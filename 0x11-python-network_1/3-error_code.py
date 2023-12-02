#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays the body of the response."""
import sys
from urllib import request, error

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as responce:
            print(responce.read().decode('UTF-8'))
    except error.HTTPError as failure:
        print('Error code:', failure.code)
