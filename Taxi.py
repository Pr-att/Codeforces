# TODO: Incomplete

num = int(input())
arr = list(map(int, input().split()))
arr.sort()
maps = {}
for i in arr:
    if i in maps:
        maps[i] += 1
    else:
        maps[i] = 1
ans = 0
if 4 in arr:
    ans += maps[4]
    maps[4] = 0
if 2 in arr:
    ans += (maps[2] // 2)
    maps[2] = (maps[2] % 2)
if 1 in arr and 3 in arr:
    var = min(maps[1], maps[3])
    ans += var
    maps[3] -= var
    maps[1] -= var
if 1 in arr and 2 in arr:
    if maps[2] == 0 and 4 >= maps[1] > 0:
        ans += 1
        maps[1] = 0
    elif maps[2] == 0 and maps[1] > 4:
        ans += (maps[1] // 4) + 1
        maps[1] = 0
    elif maps[2] == 1 and 2 >= maps[1] > 0:
        ans += 1
        maps[1] = 0
        maps[2] = 0
    elif maps[2] == 1 and 4 > maps[1] > 2:
        ans += 2
        maps[1] = 0
        maps[2] = 0
    elif maps[2] == 1 and maps[1] >= 4:
        ans += ((maps[1]) // 4) + 1
        maps[1] = 0
        maps[2] = 0
# print(maps, ans)
for key, value in maps.items():
    if key == 1 and value != 0:
        if value <= 4:
            ans += 1
        else:
            if value % 4 == 0:
                ans += (value // 4)
            else:
                ans += (value // 4) + 1
    else:
        ans += value
print(ans)

# ans = 0
# for i in range(num - 1):
#     try:
#         maps[arr[i]] -= 1
#         maps[4 - arr[i]] -= 1
#         ans += 1
#     except KeyError:
#         try:
#             maps[4 - arr[i] - 1] -= 1
#             ans += 1
#         except KeyError:
#             maps[4 - arr[i] - 2] -= 1
#             ans += 1
# print(ans)
