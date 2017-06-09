def getConversionTable():
	actualC = []
	approxC = []
	F = [0, 10,20,30,40,50,60,70,80,90,100]

	for i in range(len(F)):

		A = round(((F[i]-32)*5/9.0),1)
		B = round((F[i]-30)/2,1)

		actualC.append(A)
		approxC.append(B)

	return [F, actualC, approxC]


print getConversionTable()

