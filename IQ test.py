n = int(input())
nums = list(map(int, input().split()))
even, odd = 0, 0
even_nums = len([i for i in nums if i % 2 == 0])
if even_nums > 1:
    for j in nums:
        if j % 2 != 0:
            print(nums.index(j) + 1)
            break
else:
    for k in nums:
        if k % 2 == 0:
            print(nums.index(k) + 1)
            break
