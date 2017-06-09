'''arg1 = raw_input("Enter C or F: ")
arg2 = raw_input("Enter number: ")'''

def tempConvert(arg1, arg2):
	if arg1 == "C":
		result = fToC(arg2)
		return result
	elif arg1 == "F":
		result = cToF(arg2)
		return result
	else:
		result = "None"
		return result

	

def fToC(F):
	C = (((F - 32)*float(5)/9))
	return C

def cToF(C):
	F = (C * (float(9)/5) + 32)
	return F

#print ''' Test case 1: C = 32 '''
ans = tempConvert( "F", 100)
print ans

