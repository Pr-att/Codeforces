l1, l2, l3 = [], [], {}
for i in range(int(input())):
    a, b = map(int, input().split())
    l1.append(a)
    l2.append(b)
for i in l1:
    l3[i] = l2.count(i)
ans = 0
for j in l1:
    ans += l3[j]
print(ans)
