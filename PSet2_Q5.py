def investmentVal(investmentAmount, annualInterestRate, numberOfYears):
	monthlyInterestRate = ((annualInterestRate / 12) / 100)
	numberOfMonths = numberOfYears * 12
	investmentVal = investmentAmount * ((1 + monthlyInterestRate) ** numberOfMonths)
	print round(investmentVal, 2)

investmentVal(1000,4.25,1)
investmentVal(1500,3.25,2)
investmentVal(1000,2.25,0.5)
investmentVal(2000,4.25,3)