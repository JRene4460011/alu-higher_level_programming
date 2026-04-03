#!/usr/bin/python3
"""Display body or error code with requests"""
import requests
import sys

url = sys.argv[1]
res = requests.get(url)
if res.status_code >= 400:
    print(f"Error code: {res.status_code}")
else:
    print(res.text)
