def compoundVal6Month(MonthlySavings, AnnualinterestRate, no_of_months):
	monthlyInterestRate = ((AnnualinterestRate / 12))
	total_value = 0
	counter = 1
	while (counter <= no_of_months):
		compoundValMonth = (total_value + MonthlySavings) * (1 + monthlyInterestRate)
		total_value = compoundValMonth
		counter = counter + 1
	return compoundValMonth

ans = compoundVal6Month(100,0.05,6)
print "%.2f" % ans