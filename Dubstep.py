word = input()
p = word.split('WUB')
for i in p:
    if i == '':
        p.remove(i)
print(' '.join(p))