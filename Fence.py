m, n = map(int, input().split())
array = list(map(int, input().split()))
if n == 1:
    print(array.index(min(array)) + 1)
else:
    ans = sum(array[0: n])
    big = float("inf")
    k = 0
    if ans < big:
        big = ans
        k = 1
    for _ in range(1, m - n + 1):
        ans -= array[_ - 1]
        ans += array[_ + (n - 1)]
        if ans < big:
            big = ans
            k = _ + 1
    print(k)
