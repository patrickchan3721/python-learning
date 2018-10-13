#!/usr/bin/python

import itertools

diffmin=100
receipts = []

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

for l in range(1, len(receipts)):
   for subset in itertools.combinations(receipts, l):
      difftmp=sum(subset)%100
      if difftmp < diffmin:
         diffmin = difftmp
         receiptbest = subset

print "The receipts' value are ", receipts
print "The best combination (closest to 100 x n) is ", receiptbest
print "Difference is ", diffmin

