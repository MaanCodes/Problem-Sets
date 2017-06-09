def SgdToInr(Sgd):
	Inr = float(Sgd) * 48.29
	return float(Inr)

Sgd = float(raw_input("Enter amount in SGD: "))
print "Your amount in INR is %f" % SgdToInr(Sgd)

