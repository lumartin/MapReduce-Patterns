#!/usr/bin/python

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:

	if (len(line)) == 5 and line[0] != "user_ptr_id":
		user_ptr_id, reputation, gold, silver,bronce = line
		line = [user_ptr_id, "A", reputation, gold, silver, bronce]

	elif (len(line)) == 19 and line[0] != "id" :
		id,title, tagnames, author_id, body, node_type, parent_id, \
		abs_parent_id, added_at, score, state_string, last_edited_id, \
		last_activity_by_id, last_activity_at, active_revision_id, extra, \
		extra_ref_id, extra_count, marked = line
		line = [author_id, "B", id, title, tagnames, node_type, parent_id, \
                abs_parent_id, added_at, score, state_string, last_edited_id, \
                last_activity_by_id, last_activity_at, active_revision_id, extra, \
                extra_ref_id, extra_count, marked]
	else:
		pass

	writer.writerow(line)
