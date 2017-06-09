def compoundVal6Months(MonthlySavings, AnnualinterestRate):
	monthlyInterestRate = ((AnnualinterestRate / 12))
	compoundVal6Months = (MonthlySavings * 6) * (1 + (monthlyInterestRate/1200)) ** 6
	return compoundVal6Months


MonthlySavings = int(raw_input("Enter the monthy saving amount: "))
AnnualinterestRate = float(raw_input("Enter annual interest rate: "))
 
print "After the sixth month, the account value is %.2f" % compoundVal6Months(MonthlySavings, AnnualinterestRate)
	


