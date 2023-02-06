import collections

d = collections.defaultdict()
d['U'] = [0, 1]
d['D'] = [0, -1]
d['L'] = [-1, 0]
d['R'] = [1, 0]

for idx in range(int(input())):
    length = int(input())
    word = input()
    default = [0, 0]
    flag = 0
    for k in word:
        default[0] += d[k][0]
        default[1] += d[k][1]
        if default == [1, 1]:
            print("YES")
            flag = 1
            break
    if flag == 0:
        print("NO")
