def isPalindrome(num):
	array = str(num)
	return array == array[::-1]
    
print ( " Test case 1: 0 " )
ans = isPalindrome("arshihsra")
print ans