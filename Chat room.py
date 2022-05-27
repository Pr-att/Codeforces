string = 'hello'
word = input()
p, count = 0, 0
for i in range(len(word)):
    if word[i] == string[p]:
        p += 1
        count += 1
        if count == 5:
            break

if count == 5:
    print('YES')
else:
    print('NO')

