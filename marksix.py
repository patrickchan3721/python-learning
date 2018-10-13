from random import *


def main():
	numbers = []
	while (len(numbers) != 6):
		randnum = randrange(1,49)
		if randnum not in numbers:
			numbers.append(randnum)
	numbers.sort()
	print numbers

main()
