from random import randrange

random_number = randrange(101)

i = 1

while i == 1:

	guess = int(raw_input("I am thinking of a number between 1-100. Can you guess what it is?"))
	if guess > random_number:
		print "Lower!"
	elif guess < random_number:
		print "Higher!"
	elif guess == random_number:
		print "smart-ass"
		retry = raw_input("Do you wish to continue? Yes or No?")
		if "Yes" in retry:
			i = 1
			random_number = randrange(101)
		else:
			print "Okay, Bye!"
			i = 0
	else:
		print "That is not a valid guess. Please try again."


