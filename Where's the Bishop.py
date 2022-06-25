for _ in range(int(input())):
    y = input()
    t = []
    for i in range(8):
        y = input()
        if y == '':
            pass
        else:
            t.append(y)
    # print(t)
    for j in range(1, len(t) - 1):
        if t[j - 1].count('#') == 2 and t[j].count('#') == 1 and t[j + 1].count('#') == 2:
            # print(t[j])
            print(j + 1, t[j].find('#') + 1)
