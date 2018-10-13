#!/usr/bin/python

import itertools

diffmin=100
receipt = (284, 317, 330, 458, 488)

for l in range(1, len(receipt)):
   for subset in itertools.combinations(receipt, l):
      difftmp=sum(subset)%100
      if difftmp < diffmin:
         diffmin = difftmp
         receiptbest = subset

print "The best combination (closest to 100 x n) is ", receiptbest
print "Difference is ", diffmin
