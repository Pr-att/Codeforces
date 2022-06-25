for _ in range(int(input())):
    n, m = map(int, input().split())
    array = []
    ma = -1 * float("inf")
    Eye, J = 0, 0
    for i in range(n):
        t = list(map(int, input().split()))
        maxi = max(t)
        if maxi >= ma:
            ma = maxi
            Eye = i + 1
            J = t.index(ma) + 1
        array.append(t)
    # print(Eye, J, n, m)
    # print("\n")
    max_X = max((n - Eye), (Eye - 1)) + 1
    max_Y = max((m - J), (J - 1)) + 1
    print(max_X * max_Y)
