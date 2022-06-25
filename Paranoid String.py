string = "1001"
res = [string[i: j] for i in range(len(string))
       for j in range(i + 1, len(string) + 1)]
res.sort()
# print(len(res))
print(str(res))


def checker_01(s):
    t = ''
    i = 0
    u = len(s)
    while u != 0:
        if '01' in s:
            t += '1'
            u -= 1
        elif '10' in s:
            t += '0'
            u -= 1
        else:
            t += s[i]
    return t


print(checker_01('1001'))
