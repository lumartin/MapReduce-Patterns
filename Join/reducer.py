#!/usr/bin/python

import sys

oldKey = None
currentRep = 0
currentGold = 0
currentSilver = 0
currentBronze = 0


for line in sys.stdin:
    line = line.strip().split("\t")
    #print line
    if oldKey and line[0] != oldKey:
	if line[1] == '"A"':
		currentRep = line[2]
		currentGold = line[3]
		currentSilver = line[4]
		currentBronze = line[5]

    if len(line) > 15:
	#print line[1]
    	oldKey = line[0]
    	if line[1] == '"B"':
		#print line
		print line[2] , "\t" , line[3] , "\t" , line[4] , "\t" , \
		      line[0] , "\t" , line[5] , "\t" , line[6] , "\t" , \
		      line[7] , "\t" , line[8] , "\t" , line[9] , "\t" , \
	      	      currentRep , "\t" , currentGold , "\t" , currentSilver , "\t" , \
	     	      currentBronze , "\n\n\n\n"
    else:
	pass
	     

if oldKey != None and len(line) > 15 and line[1] == '"B"':
    print line[2] , "\t" , line[3] , "\t" , line[4] , "\t" , \
          line[0] , "\t" , line[5] , "\t" , line[6] , "\t" , \
          line[7] , "\t" , line[8] , "\t" , line[9] , "\t" , \
          currentRep , "\t" , currentGold , "\t" , currentSilver , "\t" , \
          currentBronze

