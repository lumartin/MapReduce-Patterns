#!/usr/bin/python

import sys

totalCost = 0
totalSales = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisCost = data_mapped

    if oldKey and oldKey != thisKey:
	mean = totalCost / totalSales
        print oldKey, "\t", mean
        totalCost = 0
        totalSales = 0
	

    oldKey = thisKey
    totalCost += float(thisCost)
    totalSales += 1

if oldKey: 
    mean = totalCost / totalSales
    print oldKey , "\t" , mean
