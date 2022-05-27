string = input()
word = ''
vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
for i in string:
    if i not in vowels:
        word += '.'
        if i.upper():
            word += i.lower()
        else:
            word += i
    else:
        pass

print(word)