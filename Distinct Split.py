for test in range(int(input())):
    num = int(input())
    word = input()
    MapA = {}
    MapB = {}
    arrayA = []
    arrayB = []
    tempA = 0
    tempB = 0
    for k in word:
        if k in MapA:
            arrayA.append(tempA)
        else:
            tempA += 1
            MapA[k] = 1
            arrayA.append(tempA)
    for k in word[::-1]:
        if k in MapB:
            arrayB.append(tempB)
        else:
            tempB += 1
            MapB[k] = 1
            arrayB.append(tempB)
    Max = float("-inf")
    # print(arrayA, arrayB)
    for final in range(num - 1):
        if (arrayA[final] + arrayB[num - final - 1]) > Max:
            Max = arrayA[final] + arrayB[num - final - 2]
    print(Max)