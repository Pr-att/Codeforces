for _ in range(int(input())):
    num = input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t = max(a) - max(b)
    # print('\n', t)
    if t < 0:
        print('NO')
    else:
        for i in range(len(a)):
            if a[i] - t <= 0:
                a[i] = 0
            else:
                a[i] -= t
    # print(a, b)
        if a == b:
            print('YES')
        else:
            print('NO')
