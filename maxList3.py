import sys

def maxList(x):

	maximum = -sys.maxint-1
	for element in x:
		if maximum < element:
				maximum = element
	return maximum

def maxlist(nested_list):
	l = []
	for x in nested_list:
		a = maxList(x)
		l.append(a)
		
	return l


inp = [[100] ,[1 ,7] ,[ -8 , -2 , -1] ,[2]]

print maxlist(inp)
