#!/usr/bin/env python

import sys

file=[]
last_key=None

for input_line in sys.stdin:
    input_line = input_line.strip()
    this_key, value = input_line.split("\t", 1)

    if last_key == this_key:
        file.append(value)
    else:
        if last_key: 
            print("%s\t%s" % (last_key, ",".join(file)))
        file = [value]
        last_key = this_key

if last_key:
    print("%s\t%s" % (last_key, ",".join(file)))