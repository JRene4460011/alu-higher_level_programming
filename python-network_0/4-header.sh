#!/bin/bash
# Send GET request with header and follow redirects
curl -s -L -H "X-HolbertonSchool-User-Id: 98" -X GET "$1"
