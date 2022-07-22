n, m = map(int, input().split())
a = list(map(int, input().split()))
x = [0]
for i in range(1, n):
    x.append(x[i - 1] + max(0, a[i - 1] - a[i]))
y = [0]
for i in range(-2, -(n + 1), -1):
    y.append(y[-1] + max(0, a[i + 1] - a[i]))
for k in range(m):
    t, s = map(int, input().split())
    if t > s:
        ans = y[-s] - y[-t]
    else:
        ans = x[s - 1] - x[t - 1]
    print(ans)
