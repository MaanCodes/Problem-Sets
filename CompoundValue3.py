def compoundVal6Month(MonthlySavings, AnnualinterestRate):
	monthlyInterestRate = ((AnnualinterestRate / 12))
	
	total_value = 0
	while (no_of_months <= 6 ):
		compoundValMonth = (total_value + MonthlySavings) * (1 + monthlyInterestRate)
		total_value = compoundValMonth
		no_of_months = no_of_months+1
	return compoundValMonth

MonthlySavings = int(raw_input("Enter the monthy saving amount: "))
AnnualinterestRate = float(raw_input("Enter annual interest rate: "))
no_of_months= raw_input("Enter number of months: ")

print "After the sixth month, the account value is %.2f" % compoundVal6Month(MonthlySavings, AnnualinterestRate)
