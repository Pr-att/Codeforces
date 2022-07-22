m, n = map(int, input().split())
string = input()
y = {}
for i in string:
    if i in y:
        y[i] += 1
    else:
        y[i] = 1
array = sorted(y.values())
j = len(array) - 1
ans = 0
while True:
    if n > 0:
        if array[j] > n:
            ans += (n * n)
            break
        else:
            ans += (array[j] * array[j])
            n -= array[j]
            j -= 1
    else:
        break
print(ans)
