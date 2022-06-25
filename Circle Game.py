for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    y = arr.index(min(arr))
    if n % 2 != 0:
        print('Mike')
    else:
        if y % 2 == 0:
            print('Joe')
        else:
            print('Mike')
