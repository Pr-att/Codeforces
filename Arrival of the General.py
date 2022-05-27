num = int(input())
nums = list(map(int, input().split()))
length = len(nums)
maxi, mini, a, b = max(nums), min(nums), 0, 0
for i in nums:
    if i == maxi:
        a = nums.index(i)
        break
for j in range(len(nums) - 1, 0, -1):
    if nums[j] == mini:
        b = j
        break
if a > b:
    print(a + (length - b) - 1 - 1)
else:
    print(a + (length - 1 - b))
