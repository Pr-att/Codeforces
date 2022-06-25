for _ in range(int(input())):
    n, k = map(int, input().split())
    string = input()
    count = 0
    if 'B' * k in string:
        print(0)
    elif n == k:
        print(string.count('W'))
    else:
        Max = 0
        for i in range(len(string)):
            if string[i] == 'B':
                count += 1
                Max = max(Max, count)
            elif string[i] == 'W':
                Max = max(Max, count)
                count = 0
        print(k - Max)
