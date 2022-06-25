for _ in range(int(input())):
    a, b = map(int, input().split())
    ans = abs(a - b)
    string = ''
    if a >= b:
        string += '01' * b
        string += '0' * (a - b)
    else:
        string += '10' * a
        string += '1' * (b - a)
    print(string)
