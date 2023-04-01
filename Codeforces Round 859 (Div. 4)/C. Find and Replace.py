for i in range(int(input())):
    length = int(input())
    string = input()
    Dict = {}
    flag = 0
    for index, char in enumerate(string):
        if index % 2 == 0:
            if char in Dict:
                if Dict[char] != "even":
                    flag = 1
                    break
            else:
                Dict[char] = "even"
        else:
            if char in Dict:
                if Dict[char] != "odd":
                    flag = 1
                    break
            else:
                Dict[char] = "odd"
    if flag == 1:
        print("NO")
    else:
        print("YES")
