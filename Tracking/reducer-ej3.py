#!/usr/bin/python

import sys

hitsTotal = 0
topSite = None
topHits = 0
oldKey = None


for line in sys.stdin:
    thisKey = line.strip().split()

    #if len(thisKey) != 1:
        # Something has gone wrong. Skip this line.
     #   continue

    if oldKey and oldKey != thisKey:
        #print oldKey, "\t", hitsTotal
	hitsTotal += 1
	if hitsTotal > topHits:
	   topHits = hitsTotal
           topSite = oldKey
        oldKey = thisKey;
        hitsTotal = 0
    
    oldKey = thisKey
    hitsTotal += 1 

#if oldKey != None:
print topSite, "\t", topHits

