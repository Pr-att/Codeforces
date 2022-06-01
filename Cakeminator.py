r, c = map(int, input().split())
x, y = set(), set()
for i in range(r):
    a = input()
    for j in range(len(a)):
        if a[j] == 'S':
            x.add(i)
            y.add(j)
print(r * c - len(x) * len(y))