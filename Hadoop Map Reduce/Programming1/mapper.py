#!/usr/bin/env python

import sys

for line in sys.stdin:
    keys = line.split()
    keys = list(keys)
    for i in range(len(keys) - 1):
        key = keys[i] + "," + keys[i + 1]
        value = 1
        print( "%s\t%d" % (key, value) )