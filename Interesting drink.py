def binarySearch(x, value):
    first = 0
    last = len(x)
    while first < last:
        mid = (first + last) // 2
        if x[mid] > value:
            last = mid
        else:
            first = mid + 1
    return first


n = int(input())
j = sorted(map(int, input().split()))
k = int(input())
for i in range(k):
    a = int(input())
    t = binarySearch(j, a)
    print(t)