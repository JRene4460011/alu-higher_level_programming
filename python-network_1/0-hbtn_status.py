#!/usr/bin/python3
"""
0-hbtn_status.py
Fetches a URL using urllib and displays body response info:
    - type
    - raw bytes content
    - utf-8 decoded content
"""

import urllib.request
import sys

if __name__ == "__main__":
    # Default to local server for container testing
    url = "http://0.0.0.0:5050/status"

    # If URL provided as argument, use it
    if len(sys.argv) > 1:
        url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        body = response.read()  # bytes

        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
