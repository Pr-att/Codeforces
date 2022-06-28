for _ in range(int(input())):
    m, n = map(int, input().split())
    c = 0
    array = list(map(int, input().split()))
    if n == 1:
        if m % 2 != 0:
            print(m // 2)
        else:
            print((m - 1) // 2)
    else:
        for i in range(1, len(array) - 1):
            if array[i] > array[i - 1] + array[i + 1]:
                c += 1
                i += 2
        print(c)
