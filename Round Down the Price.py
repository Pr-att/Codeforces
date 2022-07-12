for i in range(int(input())):
    num = int(input())
    k = 0
    while True:
        if num % (10 ** k) == num:
            break
        k += 1
    start = abs((10 ** (k - 1)) - num)
    print(start)
