for i in range(int(input())):
    num = input()
    p = float('inf')
    if len(num) > 2:
        for j in num:
            if int(j) < p:
                p = int(j)
        print(p)
    else:
        print(num[1])
