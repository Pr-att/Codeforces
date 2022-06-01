n, v = map(int, input().split())
u = []
for i in range(1, n + 1):
    j = list(map(int, input().split()))
    for k in range(1, j[0] + 1):
        if j[k] < v:
            u.append(i)
            break

u.sort()
if len(u) == 0:
    print(0)
else:
    print(len(u))
    for i in u:
        print(i, end=' ')
