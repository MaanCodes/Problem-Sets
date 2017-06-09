
def listSum(l):
	i = 0
	for numbers in l:
		i += numbers
	return i

def findAverage(list):
	l = []
	for x in list:
		o = float(listSum(x)) / len(x)
		l.append(o)
	overall = round(listSum(l)/len(l),2)
	return (l, overall)


ans = findAverage([[3 ,4] ,[5 ,6 ,7] ,[ -1 ,2 ,8]])
print ans