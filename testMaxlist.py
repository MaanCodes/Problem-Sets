import sys

def maxList(x):
	maximum = -sys.maxint-1
	for element in x:
		if maximum < element:
				maximum = element
	return maximum

print maxList([1, 2, 3, 5, 34])
