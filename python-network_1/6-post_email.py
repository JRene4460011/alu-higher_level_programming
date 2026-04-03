#!/usr/bin/python3
"""Send POST request with email parameter using requests"""
import requests
import sys

url = sys.argv[1]
email = sys.argv[2]
res = requests.post(url, data={"email": email})
print(res.text)
