#!/usr/bin/python

import sys,re

pattern = ["[0-9]", "[A-Z]", "[a-z]", "[^0-9A-Za-z]"]

def f(p,s):
   p1 = re.compile(p)
   for c in s:
      if p1.match(c):
         return True
   return False


if len(sys.argv[1]) == 16:
   if all(map (f, pattern,[sys.argv[1][i*4:i*4+4] for i in range(4)])):
      print ("Password ok")   
