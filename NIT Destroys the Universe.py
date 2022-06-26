for _ in range(int(input())):
    num = int(input())
    array = list(map(int, input().split()))
    count = 0
    for i in array:
        if i == 0:
            count += 1
    if count == num:
        print(0)
    elif count < num:
        i, j = 0, 1
        while 0 <= i <= num - 1 and 0 <= j <= num - 1:
            if array[i] == 0:
                i += 1
                j = i + 1
            elif array[j] != 0:
                j += 1
            else:
                break
        if num - (j - i) == count:
            print(1)
        else:
            print(2)
