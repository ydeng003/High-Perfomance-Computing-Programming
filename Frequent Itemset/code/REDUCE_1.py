#!/usr/bin/env python

import sys

last_key = None

for line in sys.stdin:
	candidate = line.strip()
	this_key, _ = candidate.split("\t")
	if last_key != this_key:
		last_key = this_key
		print("%s" % last_key)
           
