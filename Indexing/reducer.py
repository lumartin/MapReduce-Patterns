#!/usr/bin/python

import sys

generalMap = dict({})

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    try:
	map = None
	plainKey = data_mapped[1].strip()
    	if generalMap.has_key(plainKey):
 		content = generalMap.get(plainKey)
		count = content[0] + 1
		updatedMap = list(content[1])
		updatedMap.append(data_mapped[0])
		updatedContent = (len(updatedMap), updatedMap)
    		map = {plainKey : updatedContent}
    	else:
		firstContent = (1, (data_mapped[0]))
		map = {plainKey : firstContent}
		#print map

    	generalMap.update(map)
    except:
     	pass

for item in generalMap.iteritems():
	print item
