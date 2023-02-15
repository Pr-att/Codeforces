# TODO: Greedy

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

# TODO: DP

n = int(input())


def func(amount, dp, i, denoms):
    if amount == 0:
        return dp[0]
    elif amount > 0:
        temp = amount // denoms[i]
        dp[i] = temp + func(amount - (temp * denoms[i]), dp, i - 1, denoms)
        return dp[i]


array = [0] * 5
idx = 4
denomination = [1, 5, 10, 20, 100]
print(func(n, array, idx, denomination))
