for i in range(int(input())):
    n, x = map(int, input().split())
    array = list(map(int, input().split()))
    array.sort()
    k = n
    count = 0
    for j in range(n):
        if array[k] - array[j] >= x:
            count += 1
            k += 1
        else:
            print('NO')
            break
    if count == n:
        print('YES')