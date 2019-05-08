#!/usr/bin/env python

import sys

last_key = None
total = 0
THRESHOLD = 12
for line in sys.stdin:
    this_key, value = line.strip().split('\t')
    value = int(value)
    if this_key == last_key:
        total += value
    else:
        if last_key:
            if total >= THRESHOLD:
                print str(last_key) + '\t' + str(total)
	last_key = this_key
        total = value
    
if total >= THRESHOLD:
    print str(last_key)+"\t"+str(total)
