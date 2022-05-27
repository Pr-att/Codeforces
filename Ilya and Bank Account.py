num = input()
if int(num) >= 0:
    print(num)
else:
    if int(num[-2]) >= int(num[-1]):
        print(int(num[0:-2] + num[-1]))
    else:
        print(int(num[0:-1]))
