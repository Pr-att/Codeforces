a, b = map(int, input().split())
if a % 2 == 0:
    if b <= a // 2:
        print((2 * b) - 1)
    else:
        print(2 * (b - (a // 2)))
else:
    if b <= (a // 2) + 1:
        print((2 * b) - 1)
    else:
        print(2 * (b - ((a // 2) + 1)))

"""
10 3

odd first , then even second

[1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

5

[1, 3, 5, 7, 2, 4, 6]

"""
