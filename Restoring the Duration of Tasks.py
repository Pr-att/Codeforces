for _ in range(int(input())):
    num = int(input())
    s = list(map(int, input().split()))
    f = list(map(int, input().split()))
    array = [f[0] - s[0]]
    for i in range(1, len(s)):
        if s[i] > f[i - 1]:
            array.append(f[i] - s[i])
        else:
            array.append(f[i] - f[i - 1])
    for i in array:
        print(i, end=' ')
    print()
