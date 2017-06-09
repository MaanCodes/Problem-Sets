from math import *

def investmentVal(investmentAmount, annualInterestRate, numberOfYears):
	monthlyInterestRate = ((annualInterestRate / 12) / 100)
	numberOfMonths = numberOfYears * 12
	finvestmentVal = investmentAmount * ((1 + monthlyInterestRate) ** numberOfMonths)
	return finvestmentVal

investmentAmount = int(raw_input("Enter Investment Amount:"))
annualInterestRate = float(raw_input("Enter annual interest rate:"))
numberOfYears = int(raw_input("Enter number of years:"))
print "Accumulated value is %.2f" % investmentVal(investmentAmount, annualInterestRate, numberOfYears)