#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split()
    #print data 
    if len(data) == 10:
        ip, client, username, time, latency, type, request, mode, status, size = data
	#print data
        print request 

