for i in range(int(input())):
    num = int(input())
    ar = list(map(int, input().split()))
    count = 3
    flag = 1
    while True:
        if count == 0:
            break
        if ar[num - 1] == 0 and count > 1:
            print('NO')
            break
        elif ar[num - 1] != 0:
            num = ar[num - 1]
            flag += 1
        count -= 1
    if flag == 3:
        print('YES')
