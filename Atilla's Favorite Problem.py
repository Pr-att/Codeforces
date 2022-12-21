array = [-1, -2] * 3
f = len(array)
value = sum(array)
lu = len(array) - 1
final = []
count = 0
index = 1


def addition(maxi, length, ind):
    global count, f
    if length == f:
        return maxi
    if ind == length:
        ind += 1
        count += 1
        addition(maxi, length - 1, ind)
    temp = ind
    for i in range(length):
        val = array[count] + array[temp]
        if val > maxi:
            maxi = val
        array.append(val)
        count += 1
        temp += 1
    ind += 1


mami = float("-inf")
print(addition(mami, lu, index))
