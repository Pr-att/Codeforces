for i in range(int(input())):
    num = int(input())
    array = list(map(int, input().split()))
    k, j = 0, len(array) - 1
    count = 0
    cur = float("inf")
    while k <= j:
        if array[j] <= array[k] <= cur:
            cur = array[k]
            count += 1
            k += 1
        elif array[k] <= array[j] <= cur:
            cur = array[j]
            count += 1
            j -= 1
        else:
            break
    print("Yes" if count == num else "No")
