num = int(input())
num = str(num)
final = ''
if int(num[0]) == 9:
    final += '9'
elif int(num[0]) >= 9 - int(num[0]):
    final += str(9 - int(num[0]))
else:
    final += str(int(num[0]))
for i in range(1, len(num)):
    if int(num[i]) >= 9 - int(num[i]):
        final += str(9 - int(num[i]))
    else:
        final += num[i]
print(final)

