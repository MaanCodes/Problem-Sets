def nBynMultiplicationTable(N):
	output = []

	for col in range(1, N + 1):
		output.append([])
		for row in range(1,vN + 1):
			for x in output:
				x.append(row*col)
		return x


			#stuff here
			#output something lives in this area
			#output.append(????)'''
	return output

print nBynMultiplicationTable(3)


# ***DONE***
# N=3, output [[],[],[]]
# N=4, output [[],[],[],[]]

#1		2		3
#1		2		3
#1		2		3

#[[1,2,3],[1,2,3],[1,2,3]]

#1 		1		1
#2		2		2
#3		3		3













	# 1. Create N number of lists inside output
	# eg. N = 3, output = [[],[],[]]

	# 2. Insert numbers into the sublists inside the output
	# eg. [[1,2,3],[?,?,?],[?,?,?]]
	# Hint [[1,2,3], [2*1,2*2,2*3], [3*1, 3*2, 3*3]]
	# output = [[1,2,3],[2,4,6],[3,6,9]]

'''



1 2 3
2 4 6
3 6 9

1	   	2   	3 
2*1 	2*2 	2*3
3*1		3*2		3*3

1 		2		3
2		2		2
3		3		3

1		2		3		4
2*1 	2*2 	2*3		2*4
3*1		3*2		3*3		3*4
4*1		4*2		4*3		4*4
'''
