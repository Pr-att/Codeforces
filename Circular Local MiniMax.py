# TODO: not complete


for _ in range(int(input())):
    n = int(input())
    myList = tuple(map(int, input().split()))
    if n % 2 == 0:
        Dict = {}
        shortList = set(myList)
        for i in shortList:
            Dict[i] = myList.count(i)
        new = sorted(list(Dict.values()))
        if new[-1] > n / 2:
            print('NO')
            break
        else:
            List = sorted(list(myList))
            newArray = [min(List)]
            i, j, previous, c = 0, -1, 0, 1
            while True:
                if c == n - 1:
                    break
                elif previous == i:
                    previous = j - 1
                    newArray.append(List[previous])
                    j -= 1
                    c += 1
                else:
                    previous = i + 1
                    newArray.append(List[previous])
                    i += 1
                    c += 1
            print('YES')
            newArray.append(List[-1])
            print(newArray)
    else:
        print('NO')
