def UberXCost(BaseFare, TimeCost, DistanceCost):
	UberCost = BaseFare + TimeCost + DistanceCost
	return float(UberCost)

Time = float(raw_input("Input duration of journey in minutes: "))
Distance = float(raw_input("Input distance travelled during journey in Km: "))
TimeCost = Time * 0.2
DistanceCost = Distance * 0.45
BaseFare = 3

print "Your trip will cost $ %.2f, and $6 will be charged for cancelling the trip." % UberCost(BaseFare, TimeCost, DistanceCost)

