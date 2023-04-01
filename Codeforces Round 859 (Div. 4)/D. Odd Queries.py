for i in range(int(input())):
    n, q = map(int, input().split())
    array = list(map(int, input().split()))
    queries = []
    for queri in range(q):
        queries.append(tuple(map(int, input().split())))
    for j in range(1, n):
        array[j] += array[j - 1]
    for k in queries:
        if k[0] == 1:
            var = array[k[1] - 1]
        else:
            var = array[k[1] - 1] - array[k[0] - 2]
        temp = array[-1] - var + (k[2] * ((k[1] - k[0]) + 1))
        if temp % 2 != 0:
            print("YES")
        else:
            print("NO")

