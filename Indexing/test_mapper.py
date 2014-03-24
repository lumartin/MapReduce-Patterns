#!/usr/bin/python

import sys
import csv
import re

def mapper():
	reader = csv.reader(sys.stdin, delimiter='\t', lineterminator='\n', quoting = csv.QUOTE_NONE)

	for line in reader:
		body = line[4]
		print "LINEA", line
        #if "\r" not in body: 
	#print line[0] , "\t" , re.split(r"[\n\s\"\.\t\?\!<>[\]()$\/=-\\]", body)
  # except:
#	pass

def main():
	try:
		mapper()
	except:
		pass

main()
