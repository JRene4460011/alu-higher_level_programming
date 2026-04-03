#!/usr/bin/python3
"""Search user via POST request and display id/name"""
import requests
import sys

q = sys.argv[1] if len(sys.argv) > 1 else ""
res = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

try:
    data = res.json()
    if not data:
        print("No result")
    else:
        print(f"[{data.get('id')}] {data.get('name')}")
except ValueError:
    print("Not a valid JSON")
