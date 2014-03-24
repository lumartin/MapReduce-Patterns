#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) == 10:
        ip, client, username, time, latency, type, request, mode, status, size = data
        print request 

