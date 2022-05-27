from collections import Counter

n = int(input())
word = input()
new_word = ''
c = 0
t = len(word)
a = Counter(word)
print(a)
keys = [i for i in a.keys()]
print(keys)
for i in a.values():
    if i % n == 0:
        c += 1
    else:
        c = -1
        print(c)
        break
if c == (int(t / n)):
    j = 0
    while len(new_word) != len(word):
        try:
            new_word += (key for key, value in a.items())
            a[j] -= 1
        except IndexError:
            j += 1
    print(new_word, end='')
