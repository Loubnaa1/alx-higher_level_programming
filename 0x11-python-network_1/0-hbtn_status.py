#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen
    ('https://alx-intranet.hbtn.io/status') as response:
        core = response.read()
    print("Body response:")
    print("\t- type:", type(core))
    print("\t- content:", core)
    print("\t- utf8 content:", core.decode('utf-8'))
