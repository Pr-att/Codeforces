word1 = input()
word2 = input()
c = 0
for i in range(len(word1)):
    if word1[i].lower() > word2[i].lower():
        print(1)
        break
    elif word1[i].lower() < word2[i].lower():
        print(-1)
        break
    else:
        c += 1
if c == len(word1):
    print(0)