noOfCoins = int(input())
coins = list(map(int, input().split()))
coinsWorth = (sum(coins) // 2) + 1
coins.sort()
i, ans, no = -1, 0, 0
while True:
    if ans < coinsWorth:
        ans += coins[i]
        no += 1
        i -= 1
    elif ans >= coinsWorth:
        break
    else:
        continue
print(no)