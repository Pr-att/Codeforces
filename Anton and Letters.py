letters = input()[1: -1]
if letters == '':
    print(0)
else:
    u = letters.split(',')
    for k in range(len(u)):
        u[k] = u[k].strip()
    print(len(set(u)))