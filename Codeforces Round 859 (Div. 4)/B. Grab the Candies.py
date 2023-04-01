for i in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    mihai, bianca, flag = 0, 0, 0
    for j in array:
        if j % 2 == 0:
            mihai += j
    for k in array:
        if k % 2 != 0:
            bianca += k
            if bianca >= mihai:
                flag = 1
                break
    if flag == 1:
        print("NO")
    else:
        print("YES")

