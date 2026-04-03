#!/usr/bin/python3
"""
0-hbtn_status.py
Fetches a URL using urllib and displays the body response info:
    - type
    - raw bytes content
    - utf-8 decoded content
"""

import urllib.request


if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"  # local server for testing

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()  # bytes

            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode("utf-8")))
    except Exception as e:
        print("Error:", e)
