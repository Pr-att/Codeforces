myList = list(map(int, input().split()))
# myList = [10, 3, 5, 1]
totalDistance = myList[0]
specialTicketPrice = myList[3]
specialTicketRides = myList[1]
costOneSpecialRide = specialTicketPrice / specialTicketRides
costOneRide = myList[2]
ans, c = 0, 0
if costOneSpecialRide <= costOneRide:
    while True:
        if totalDistance == 0:
            break
        elif totalDistance < 0:
            ans -= specialTicketPrice
            totalDistance += specialTicketRides
            c = 1
            break
        else:
            ans += specialTicketPrice
            totalDistance -= specialTicketRides
    if c == 1:
        if (ans + (totalDistance * costOneRide)) < (ans + specialTicketPrice):
            ans += (totalDistance * costOneRide)
        else:
            ans += specialTicketPrice

else:
    ans = totalDistance * costOneRide
print(ans)

