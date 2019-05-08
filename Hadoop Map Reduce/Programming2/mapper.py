#!/usr/bin/env python
import os
import sys

filepath = os.environ["map_input_file"] 
file = os.path.split(filepath)[-1]


for line in sys.stdin:
    keys = line.split()
    for key in keys:
        print("%s\t%s" % (key, file))

