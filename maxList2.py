import sys

def maxList(x):
	count = 0
	if x == []:
		return "None, None"
	else:
		maximum = -sys.maxint-1
		minimum = sys.maxint
		
		for element in x:
			if maximum < x[count]:
				maximum = x[count]
			if minimum > x[count]:
				minimum = x[count]
			count += 1

	return minimum, maximum

ans = maxList([1])
print ans