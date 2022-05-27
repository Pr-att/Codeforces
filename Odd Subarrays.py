# TODO: TLE.

for _ in range(int(input())):
    n = int(input())
    myList = list(map(int, input().split()))
    i, j, inversion, p = 0, 1, 0, []
    while i != len(myList) - 1:
        try:
            if myList[i] <= myList[j]:
                inversion = 0
                p.append(inversion)
                i += 1
                j += 1
            else:
                inversion += 1
                j += 1
        except IndexError:
            p.append(inversion)
            i += 1
            j = i + 1
    answer = 0
    for i in p:
        if i % 2 != 0:
            answer += 1
    print(answer)
