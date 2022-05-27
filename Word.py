word = input()
up, low = 0, 0
w = [i for i in word]
for i in w:
    if i.isupper():
        up += 1
    elif i.islower():
        low += 1
if up > low:
    print(word.upper())
else:
    print(word.lower())