#!/usr/bin/python3
"""Display GitHub user id using Basic Auth"""
import requests
import sys

username = sys.argv[1]
token = sys.argv[2]

res = requests.get("https://api.github.com/user", auth=(username, token))
if res.status_code == 200:
    print(res.json().get("id"))
else:
    print("None")
