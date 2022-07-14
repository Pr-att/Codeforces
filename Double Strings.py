for _ in range(int(input())):
    num = int(input())
    array = [input() for k in range(num)]
    newArray = set(array)
    final = []
    for x in array:
        for i in range(1, len(x)):
            if x[:i] in newArray and x[i:] in newArray:
                final.append("1")
                break
        else:
            final.append("0")
    print("".join(final))
