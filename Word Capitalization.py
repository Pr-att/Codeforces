word = input().split()
for i in range(len(word)):
    word = word[i].replace(word[i][0], word[i][0].upper(), 1)
print("".join(word))