#!/usr/bin/python3
"""Display X-Request-Id using requests"""
import requests
import sys

url = sys.argv[1]
res = requests.get(url)
print(res.headers.get("X-Request-Id"))
