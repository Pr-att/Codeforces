amount = int(input())
deno = [1, 5, 10, 20, 100]
j = len(deno) - 1
count = 0
if amount >= 100:
    count += amount // 100
    amount -= count * 100
while amount != 0:
    if amount // deno[j] >= 1:
        amount -= deno[j]
        count += 1
    else:
        j -= 1
print(count)
