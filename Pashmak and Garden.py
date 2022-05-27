x1, y1, x2, y2 = map(int, input().split())
distance1 = x2 - x1
distance2 = y2 - y1
p = [x1, x2, x2, y2]
if len(set(p)) > 2:
    print(-1)
else:
    if distance1 > 0 and distance2 > 0:
        print(x1, y2, x2, y1)
    elif distance1 > 0 and distance2 == 0:
        print(distance1, distance1, x1, distance1)
    elif distance2 > 0 and distance1 == 0:
        print(distance2, distance2, distance2, y1)
