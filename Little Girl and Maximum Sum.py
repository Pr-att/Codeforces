""" TLE """

# totalNums, noOfQueries = map(int, input().split())
# numsArray = list(map(int, input().split()))
# Queries = []
# for idx in range(noOfQueries):
#     Temp = list(map(int, input().split()))
#     Queries.append(Temp)
# numsArray.sort()
# Array = [0] * (totalNums + 1)
# for id2 in range(noOfQueries):
#     Array[Queries[id2][0] - 1] += 1
#     Array[Queries[id2][1]] -= 1
# for id3 in range(1, totalNums + 1):
#     Array[id3] += Array[id3 - 1]
# Array.pop()
# Final = []
# ty = [i for i in range(len(Array))]
# temp = list(zip(Array, ty))
# temp.sort()
# final = [0] * (len(Array))
# for k in range(len(Array)):
#     final[temp[k][1]] = numsArray[k]
# Sum = 0
# final.insert(0, 0)
# for f in range(1, totalNums + 1):
#     final[f] += final[f - 1]
# for id5 in range(noOfQueries):
#     Sum += final[Queries[id5][1]] - final[Queries[id5][0] - 1]
# print(Sum)

""" TLE """

# n, q = map(int, input().split())
# l = list(map(int, input().split()))
# d = [0] * n
#
# l.sort()
# for i in range(q):
#     lef, r = map(int, input().split())
#     d[lef - 1] += 1
#     if r < n:
#         d[r] -= 1
#
# for i in range(1, n):
#     d[i] += d[i - 1]
#
# d.sort()
# ans = 0
#
# for i in range(n):
#     ans += d[i] * l[i]
#
# print(ans)
