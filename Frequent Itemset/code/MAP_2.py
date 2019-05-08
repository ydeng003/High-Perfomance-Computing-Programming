#!/usr/bin/env python
import sys


freItems = []    #list of frequent item  
l = []        
f = open('freqItemsets', 'r')
while 1:
    line = f.readline().strip()
    if not line:
        break
    l1,l2 = line.split(',')
    l = [l1,l2]
    l = set(l)
    freItems.insert(0,l)


baskets = []
pairs = {}
for line in sys.stdin:
    basket = line.split()
    for freItem in freItems:
        if freItem.issubset(basket):
            freItem = list(freItem)
            pairs.setdefault(str(freItem),0)
            pairs[str(freItem)] += 1
for i in pairs:
    print( '%s\t%d' % (i, pairs[i]))

