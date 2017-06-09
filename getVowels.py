def getVowels(sentence):
	d = {}
	for x in sentence:
		if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
			if x in d.keys():
				d[x] += 1
			else:
				d[x] = 1

	return d



print getVowels("aeiouaeiouaeiou")


