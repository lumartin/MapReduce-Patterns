#!/usr/bin/python

import sys

salesTotal = 0
salesNumber = 0

for line in sys.stdin:
    data_mapped = line.strip()

    salesTotal += float(data_mapped)
    salesNumber += 1

print salesTotal, "\t", salesNumber

