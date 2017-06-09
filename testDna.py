d = {"A":1, "B":3, "C":4}
teststring = "123ABC"

for x in teststring:
	if x in d.keys():
		print "this is something that is in d"
	else:
		print "this is something that is not in d"