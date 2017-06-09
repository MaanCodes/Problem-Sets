def windChillTemp(OutTemp, WindSpeed):
	windChillTemp = 35.74 + (0.6215 * OutTemp) - (35.75 * (WindSpeed**0.16)) + (0.4275 * (OutTemp) * (WindSpeed**0.16))
	return float(windChillTemp)

OutTemp = float(raw_input("Input a temperature between -58F and 41F: "))
WindSpeed = float(raw_input("Input a Wind Speed greater than or equal to 2: "))

print "The Wind Chill index is : %.11f" % windChillTemp(OutTemp, WindSpeed)