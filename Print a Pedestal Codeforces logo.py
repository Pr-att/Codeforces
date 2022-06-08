for _ in range(int(input())):
    num = int(input())
    first = (num // 3) - 1
    second = (num + 1) // 3
    third = ((num + 2) // 3) + 1
    print(second, third, first)