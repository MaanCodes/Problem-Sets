def check2(n1, n2, n3, x):
	if(x>n1 and x>n2 and x < n3):
		return True
	else:
		return False

ans = check2(1, 4, 5, 7)
print ans