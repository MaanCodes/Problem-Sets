def BaseCounts(dna):
	d = {}
	for x in dna:
		if x == "A" or x == "C" or x == "G" or x == "T": 
			if x in d.keys() :
				d[x] += 1 
			else:
				d[x] = 1
		else:
			return "The input DNA string is invalid"
	return d


print BaseCounts("AACGT") 
