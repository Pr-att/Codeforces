n = int(input())
children = list(map(int, input().split()))
teams, myDict, array = 0, {}, []
for i in children:
    if i in myDict:
        myDict[i] += 1
    else:
        myDict[i] = 1
if len(myDict.keys()) == 3:
    n = min(myDict.values())
    print(n)
    for j in range(n):
        u = [children.index(i) for i in range(1, 4) if i in children]
        for i in range(len(u)):
            children[u[i]] = 0
        array.append(u)

    for k in array:
        for h in k:
            print(h + 1, end=' ')
        print("")
else:
    print(0)
