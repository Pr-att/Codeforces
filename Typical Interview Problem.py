for test in range(int(input())):
    n = int(input())
    word = input()
    string = ""

    for i in range(1, 10001):
        if i % 3 == 0 and i % 5 == 0:
            string += "FB"
        elif i % 3 == 0:
            string += "F"
        elif i % 5 == 0:
            string += "B"
    if word in string:
        print("YES")
    else:
        print("NO")
