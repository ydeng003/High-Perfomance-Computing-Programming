#!/usr/bin/env python

import sys

last_key = None
last_value = 0
final_key = None
final_value = 0
this_value = 0

for input_line in sys.stdin:
    input_line = input_line.strip()
    this_key, value = input_line.split("\t", 1)
    value = int(value)
    
    if last_key == this_key:
        this_value += value
    else:
        last_value = this_value
        last_key = this_key
        this_value = value
        if last_value > final_value:
            final_key = last_key
            final_value = last_value
            
print( "%s\t%d" % (final_key, final_value) )