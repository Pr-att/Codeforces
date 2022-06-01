array = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    array.append([a, b])
flag = 0
array.sort()
for j in range(0, len(array) - 1):
    if array[j][0] < array[j + 1][0] and array[j][1] > array[j + 1][1]:
        flag = 1
        break
    else:
        flag = 0
if flag == 1:
    print("Happy Alex")
else:
    print("Poor Alex")
