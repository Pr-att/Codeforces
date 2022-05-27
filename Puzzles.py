a, b = map(int, input().split())
list1 = list(map(int, input().split()))
list1.sort()
test = (b - a) + 1
test2 = a
j = 0
array, myDict = [], {}
maxi, mini = float("inf"), -1 * float("inf")
for i in range(test):
    while test2 != 0:
        array.append(list1[j])
        j += 1
        test2 -= 1
    myDict[i] = max(array) - min(array)
    array = []
    test2 = a
    j = i + 1
print(min(myDict.values()))