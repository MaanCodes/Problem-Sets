def yearsDays(minutes, years, days):
	

	return float(years and days)

minutes = float(raw_input("Input the number of minutes: "))
days = int((minutes / 1440) % 365)
years = int(minutes / (365 * 1440))

print " %d minutes is approximately %d years and %d days" % (minutes, years, days)

print (years, days)