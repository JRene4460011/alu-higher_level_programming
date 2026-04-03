#!/usr/bin/python3
"""Display value of X-Request-Id in response header"""

import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    print(response.getheader("X-Request-Id"))
