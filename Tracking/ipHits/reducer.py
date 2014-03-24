#!/usr/bin/python

import sys

hitsTotal = 0
oldKey = None

for line in sys.stdin:
    thisKey = line.strip()

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", hitsTotal
        oldKey = thisKey;
        hitsTotal = 0

    oldKey = thisKey
    hitsTotal += 1

if oldKey != None:
    print oldKey, "\t", hitsTotal

