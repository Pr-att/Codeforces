n = int(input())
l1 = list(map(int, input().split()))
lt = [0] * n
for i in range(n):
    lt[l1[i] - 1] = i + 1

for i in lt:
    print(i, end=' ')