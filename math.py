#!/usr/bin/python

import itertools

numbers = [x for x in range(1,10)]
numbers_ordered = []

for order in itertools.permutations(numbers, 9):
        fraction1 = float(order[0]) / (int(str(order[1]) + str(order[2])))
        fraction2 = float(order[3]) / (int(str(order[4]) + str(order[5])))
        fraction3 = float(order[6]) / (int(str(order[7]) + str(order[8])))
        sum = fraction1 + fraction2 + fraction3
        if sum == 1:
		print order
