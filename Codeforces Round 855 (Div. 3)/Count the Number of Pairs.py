for test in range(int(input())):
    length, k = map(int, input().split())
    word = input()
    Map = {}
    for i in word:
        if i in Map:
            Map[i] += 1
        else:
            Map[i] = 1
    res = 0
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter in Map and letter.upper() in Map:
            temp = min(Map[letter], Map[letter.upper()])
            Map[letter] -= temp
            Map[letter.upper()] -= temp
            res += temp
    additional = 0
    for key, val in Map.items():
        additional += val // 2
    if additional <= k:
        print(res + additional)
    else:
        print(res + k)
