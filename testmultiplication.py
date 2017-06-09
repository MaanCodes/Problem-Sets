def multiplicationTable(N):
	output = []

	for col in range(1,N+1):
		output.append([])
		if N < 2:
			return "None"
		else:
			for row in range(1,N+1):
				output[col-1].append(row*col)

	return output

print multiplicationTable(7)
