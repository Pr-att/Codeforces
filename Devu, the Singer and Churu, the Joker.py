a, b = map(int, input().split())
myList = list(map(int, input().split()))
ans, jokes_co = 0, 0
for i in myList:
    ans += i + 10
    jokes_co += 2
jokes_co -= 2
ans -= 10
if ans < b:
    print(jokes_co + ((b - ans) // 5))
elif ans == b:
    print(jokes_co)
else:
    print(-1)