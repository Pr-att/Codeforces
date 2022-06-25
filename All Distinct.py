for _ in range(int(input())):
    t = input()
    array = list(map(int, input().split()))
    newArray = []
    lengthArray = len(array)
    for i in array:
        if i in newArray:
            pass
        else:
            newArray.append(i)
    r = lengthArray - len(newArray)
    if r % 2 == 0:
        print(len(newArray))
    else:
        print(len(newArray) - 1)
