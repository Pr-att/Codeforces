for _ in range(int(input())):
    array = list(map(int, input().split()))
    a = array[0]
    print(len([array[i] for i in range(1, len(array)) if array[i] > a]))
