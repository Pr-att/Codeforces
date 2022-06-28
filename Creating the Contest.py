num = int(input())
array = list(map(int, input().split()))
i, j = 0, 1
long = float("-inf")
while True:
    if j >= num:
        long = max(long, (j - i))
        break
    if array[j] <= (2 * array[j - 1]):
        j += 1
    else:
        long = max(long, (j - i))
        i = j
        j = i + 1
print(long)