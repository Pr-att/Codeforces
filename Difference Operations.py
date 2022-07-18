for i in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    flag = True
    for j in ar:
        if j % ar[0] != 0:
            flag = False
        else:
            pass
    if flag:
        print('YES')
    else:
        print('NO')
