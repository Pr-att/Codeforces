def getMEX(a):
    n = len(a)
    b = a
    hashmap = set(b)
    for k in range(0, n + 2):
        if k not in hashmap:
            return k


for _ in range(int(input())):
    num = int(input())
    array = list(map(int, input().split()))
    if num < 2:
        if num == 0:
            print(0)
        else:
            print(1)
    else:
        i, j, count = 0, 0, 0
        while 0 <= i <= j <= num - 1:
            if j == num - 1 or array[j] == 0:
                if getMEX(array[i: j]) == 0 and len(array[i: j]) > 0:
                    count += 1
                i = j + 1
                j = i
            elif array[j] > 0:
                j += 1
        print(count)


