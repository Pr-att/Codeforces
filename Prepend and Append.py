for test in range(int(input())):
    num = int(input())
    finalWord = input()
    i, j = 0, num - 1
    while i < j:
        if (finalWord[i] == '0' and finalWord[j] == '1') or (finalWord[i] == '1' and finalWord[j] == '0'):
            i += 1
            j -= 1
        else:
            break
    print(j - i + 1)



