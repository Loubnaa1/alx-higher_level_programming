#!/usr/bin/python3
""" Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter."""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) == 1:
        tmp = ""
    else: 
        tmp = sys.argv[1]
    donne = {"q": tmp}

    request = requests.post("http://0.0.0.0:5000/search_user", data=donne)
    try:
        responce = request.json()
        if responce == {}:
            print("No result")
        else:
            print("[{}] {}".format(responce.get("id"), responce.get("name")))
    except ValueError:
        print("Not a valid JSON")
