def compoundVal6Month(MonthlySavings, AnnualinterestRate):
	monthlyInterestRate = ((AnnualinterestRate / 12))
	compoundVal1Month = MonthlySavings * (1 + monthlyInterestRate)
	compoundVal2Month = MonthlySavings + compoundVal1Month * (1 + monthlyInterestRate)
	compoundVal3Month = MonthlySavings + compoundVal2Month * (1 + monthlyInterestRate)
	compoundVal4Month = MonthlySavings + compoundVal3Month * (1 + monthlyInterestRate)
	compoundVal5Month = MonthlySavings + compoundVal4Month * (1 + monthlyInterestRate)
	compoundVal6Month = MonthlySavings + compoundVal5Month * (1 + monthlyInterestRate)
	return compoundVal6Month

MonthlySavings = int(raw_input("Enter the monthy saving amount: "))
AnnualinterestRate = float(raw_input("Enter annual interest rate: "))

print "After the sixth month, the account value is %.2f" % compoundVal6Month(MonthlySavings, AnnualinterestRate)