for i in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    letter = ['B'] * m
    string = ''
    maps = {}
    for k in array:
        pos1, pos2 = k - 1, m - k
        mini = min(pos1, pos2)
        maxi = max(pos1, pos2)
        if letter[maxi] != 'A' and letter[mini] != 'A':
            letter[mini] = 'A'
        else:
            letter[maxi] = 'A'

    print(''.join(letter))