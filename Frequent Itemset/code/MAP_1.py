#!/usr/bin/env python
import sys

def createC1(dataset):
	"Create a list of candidate item sets of size one."
	c1 = []
	for transaction in dataset:
		for item in transaction:
			if not [item] in c1:
				c1.append([item])
	c1.sort()
	#frozenset because it will be a ket of a dictionary.
	return map(frozenset, c1)
 
 
def scanD(dataset, candidates, min_support):
	"Returns all candidates that meets a minimum support level"
	sscnt = {}
	for tid in dataset:
		for can in candidates:
			if can.issubset(tid):
				sscnt.setdefault(can, 0)
				sscnt[can] += 1
 
	retlist = []
	support_data = {}
	for key in sscnt:
		support = sscnt[key] 
		if support >= min_support:
			retlist.insert(0, key)
		support_data[key] = support
	return retlist, support_data

def aprioriGen(freq_sets, k):
	"Generate the joint transactions from candidate sets"
	retList = []
	lenLk = len(freq_sets)
	for i in range(lenLk):
		for j in range(i + 1, lenLk):
			L1 = list(freq_sets[i])[:k - 2]
			L2 = list(freq_sets[j])[:k - 2]
			L1.sort()
			L2.sort()
			if L1 == L2:
				retList.append(freq_sets[i] | freq_sets[j])
	return retList


baskets = []
keys = []
for line in sys.stdin:
    basket = line.split()
    baskets.insert(0,basket)
c1 = createC1(baskets)
baskets = map(set,baskets)
f,_ = scanD(baskets,c1,6)
dual_1 = aprioriGen(f,2)
retlists,_ = scanD(baskets,dual_1,6)

for retlist in retlists:
	retlist = list(retlist)
	keys.insert(0,retlist)
value = 1
for key in keys:
    print( '%s,%s\t%d' % (key[0], key[1] , value))

