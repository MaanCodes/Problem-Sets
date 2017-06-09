

def UberCost(BaseFare, TimeCost, DistanceCost, MinimumCost):
	UberCost = BaseFare + TimeCost + DistanceCost
	if UberCost < MinimumCost:
		return float(MinimumCost)
	else:
		return float(UberCost)

x = True

while x:
	print "What type of uber would you like to take? (UberX, UberXL)"
	choice = raw_input("> ")
	if choice == "UberX":
		Time = float(raw_input("Input duration of journey in minutes: "))
		Distance = float(raw_input("Input distance travelled during journey in Km: "))
		TimeCost = Time * 0.2
		DistanceCost = Distance * 0.45
		BaseFare = 3
		MinimumCost = 3
		x = False
		print "Your trip will cost $ %.2f, and $6 will be charged for cancelling the trip." % UberCost(BaseFare, TimeCost, DistanceCost, MinimumCost)

	elif choice == "UberXL" :
		Time = float(raw_input("Input duration of journey in minutes: "))
		Distance = float(raw_input("Input distance travelled during journey in Km: "))
		TimeCost = Time * 0.35
		DistanceCost = Distance * 0.8
		BaseFare = 5
		MinimumCost = 8
		x = False
		print "Your trip will cost $ %.2f, and $6 will be charged if you cancel the trip." % UberCost(BaseFare, TimeCost, DistanceCost, MinimumCost)


	else:
		print "You may consider using UberX, as it is a cheaper choice."
