


while True:
	Marks = int(raw_input("Please input your marks: "))
	if Marks >= 90 :
		print "Your grade is an A."
	elif Marks >= 80:
		print "Your grade is a B."
	elif Marks >= 70 :
		print "Your grade is a C."
	elif Marks >= 60  :
		print "Your grade is a D."
	elif Marks >= 50 :
		print "Your grade is an E."
	elif Marks == -1:
		print "Okay, Bye."
		break
	else:
		print "None"