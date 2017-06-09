
def matrixTranspose(nested_list):
	y = []
	l = []
	c = []
	for x in nested_list:
		l.append(x[0])
		y.append(x[1])
		c.append(x[2])
	return (l, y, c)

print matrixTranspose([[1 ,2 ,3] , [4 ,5 ,6] , [7 ,8 ,9]]) 