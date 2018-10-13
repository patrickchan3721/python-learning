#!/usr/bin/python

import sys,re

def check_pattern(pos, pattern, str1):
	for c in str1[pos[0]-1:pos[1]]:
		pattern1 = re.compile(pattern)
		if pattern1.match(c):
			return True
	return False

if len(sys.argv[1]) == 16:
	if all([check_pattern((1,4), "[0-9]", sys.argv[1]),check_pattern((5,8), "[A-Z]", sys.argv[1]),check_pattern((9,12), "[a-z]", sys.argv[1]),check_pattern((13,16), "[^a-zA-Z0-9]", sys.argv[1])]):
		print ("Password ok")
