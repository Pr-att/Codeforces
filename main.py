# for _ in range(int(input())):
#     num = int(input())
#     array = list(map(int, input().split()))
#     count = 0
#     for j in range(1, len(array)):
#         if array[j] == 0 and array[j - 1] != 0:
#             array[j] += 1
#             array[j - 1] -= 1
#             count += 1
#     for k in range(len(array) - 1):
#         if array[k] == 0:
#             pass
#         else:
#             count += array[k]
#     print(count)

