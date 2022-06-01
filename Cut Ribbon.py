n, a, b, c = map(int, input().split())
d = [a, b, c]
l = [-1] * (n + 1)
l[0] = 0
for i in d:
    for j in range(i, n + 1):
        if l[j - i] != -1:
            l[j] = max(l[j - i] + 1, l[j])
print(l[n])
