# Dreamoon and Stairs

m, n = map(int, input().split())
move, total = 0, 0
if m % 2 == 0:
    total = m / 2
else:
    total = (m - 1) / 2
while True:
    if total > m:
        print(-1)
        break
    elif total % n == 0 and (total * 2) >= m:
        print(int(total))
        break
    else:
        total += 1
