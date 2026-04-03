#!/usr/bin/python3
"""Fetch https://alu-intranet.hbtn.io/status using requests"""
import requests

url = "https://alu-intranet.hbtn.io/status"
res = requests.get(url)
body = res.text
print("Body response:")
print(f"\t- type: {type(body)}")
print(f"\t- content: {body}")
