# from itertools import combinations
#
# noOfTestCases = int(input())
# for _ in range(noOfTestCases):
#     noOfMonsters = int(input())
#     monsters = list(map(int, input().split()))
#     monsters.sort()
#     print(monsters)
#     mean = sum(monsters) / len(monsters)
#     diff = sum(monsters) - (mean * (noOfMonsters - 2))
#     print(f'Mean: {mean} \t Diff: {diff}')
#     count = 0
#     if max(monsters) == min(monsters):
#         print(f'{len(list(combinations(monsters, 2)))}')
#     else:
#         print(len([i for i in list(combinations(monsters, 2)) if sum(i) == diff]))

# from itertools import combinations
#
# noOfTestCases = int(input())
# for _ in range(noOfTestCases):
#     noOfMonsters = int(input())
#     monsters = list(map(int, input().split()))
#     monsters.sort()
#     mean = sum(monsters) / len(monsters)
#     diff = sum(monsters) - (mean * (noOfMonsters - 2))
#     count = 0
#     if max(monsters) == min(monsters):
#         print(f'{len(list(combinations(monsters, 2)))}')
#     else:
#         ans, j, k = 0, 0, -1
#         while True:
#             try:
#                 ans = monsters[j] + monsters[k]
#                 if monsters[j] >= monsters[k]:
#                     break
#                 elif ans == diff:
#                     count += 1
#                     k -= 1
#                 elif ans >= diff:
#                     k -= 1
#                 else:
#                     j += 1
#             except IndexError:
#                 break
#         print(count)

for _ in range(int(input())):
    num = int(input())
    array = list(map(int, input().split()))
    ans = 0
    for one in array:
        ans += one
    initial = ans / num
    getAns = ans - ((num - 2) * initial)
    hashmap = {}
    for i in array:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    if getAns == int(getAns):
        count = 0
        for j in hashmap:
            if getAns - j in hashmap:
                One = j
                Two = int(getAns - j)
                if One == Two:
                    count += sum([i for i in range(hashmap[One])])
                else:
                    count += hashmap[One] * hashmap[Two]
                hashmap[One] = 0
                hashmap[Two] = 0
        print(count)

    else:
        print(0)