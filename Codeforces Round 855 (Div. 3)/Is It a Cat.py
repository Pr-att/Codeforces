end = "meow"
for test in range(int(input())):
    length = int(input())
    word = input().lower()
    array = []
    i, j = 0, 0
    while j < length:
        if word[i] != word[j]:
            array.append(word[i])
            i = j
        j += 1
    array.append(word[-1])
    start = "".join(array)
    print("YES" if start == end else "NO")
