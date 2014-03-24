#!/usr/bin/python

import sys

categoriesTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", categoriesTotal
        oldKey = thisKey;
        categoriesTotal = 0

    oldKey = thisKey
    categoriesTotal += float(thisSale)

if oldKey != None:
    print oldKey, "\t", categoriesTotal

