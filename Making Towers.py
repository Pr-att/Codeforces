t = int(input())
for i in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    array = [k - 1 for k in array]
    final = [0] * n
    pos = [-1] * n
    for j in range(n):
        if pos[array[j]] == -1:
            pos[array[j]] = j
            final[array[j]] = 1
        elif (j - pos[array[j]]) % 2:
            pos[array[j]] = j
            final[array[j]] += 1
    print(*final)