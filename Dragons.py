s, n = map(int, input().split())
# s, n = 2 , 2
hashmap = []
for _ in range(n):
    a, b = map(int, input().split())
    hashmap.append([a, b])
new = sorted(hashmap)
ans, final = s, 0
for i in range(len(new)):
    if ans > new[i][0]:
        ans += new[i][1]
    else:
        final = 1
        break

if final == 1:
    print('NO')
else:
    print('YES')
