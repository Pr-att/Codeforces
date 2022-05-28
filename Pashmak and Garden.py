x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4, count = 0, 0, 0, 0, 0
distanceX = abs(x2 - x1)
distanceY = abs(y2 - y1)
if distanceX == 0:
    k = distanceY
    x3 = x1 + k
    y3 = min(y1, y2)
    x4 = x1 + k
    y4 = max(y1, y2)
elif distanceY == 0:
    k = distanceX
    x3 = min(x1, x2)
    y3 = y1 + k
    x4 = max(x1, x2)
    y4 = y1 + k
else:
    if distanceX != distanceY:
        count = 1
    else:
        x3 = x1
        y3 = y2
        x4 = x2
        y4 = y1
if count == 1:
    print(-1)
else:
    print(x3, y3, x4, y4)
