#!/usr/bin/python

import itertools

receipts = []
subsets = []

while True:
   receipttmp = raw_input("Enter the value of receipt: ")
   if receipttmp == "":
      break
   try:
      receipt = float(receipttmp)
   except ValueError:
      print "This is not a valid number"
   else:
      receipts.append(receipt)

for l in range(1, len(receipts)+1):
   for j in itertools.combinations(receipts, l):
      subsets.append(j)

sorted_subsets = sorted(subsets, key = lambda x : sum(x)%100)

for i in sorted_subsets:
   print sum(i)%100,
   print(i) 
