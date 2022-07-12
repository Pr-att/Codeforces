for i in range(int(input())):
    num = int(input())
    p = list(map(int, input().split()))
    for j in range(num):
        m, word = input().split()
        for k in word:
            if k == 'D' and p[j] == 9:
                p[j] = 0
            elif k == 'D':
                p[j] += 1
            elif k == 'U' and p[j] == 0:
                p[j] = 9
            elif k == 'U':
                p[j] -= 1
    for _ in p:
        print(_, end=' ')
    print()
