#!/usr/bin/python

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')#, lineterminator='\N', quoting = csv.QUOTE_NONE)
#writer = csv.writer(sys.stdout, delimiter=',', quotechar='"')

for line in reader:
   try:
	body = line[4]       
	wordList = re.split(r"[\,\n\s\"\.\t\?\!<>[\]()$\/=\-\\\';]", body)
	for word in wordList:
		if word <> '':
			print word.lower() , "\t" , line[0]
   except:
	pass
