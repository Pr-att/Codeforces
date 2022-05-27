for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    length = len(nums)
    nums.sort()
    i, j, count = 0, 0, 0
    ans = 0
    for k in range(length):
        for i in range(length - 1):
            if j > length - 1:
                j = 0
            ans += nums[j]
            j += 1
        if j > length - 1:
            j = 0
        if ans / (length - 1) == nums[j]:
            print('YES')
            break
        else:
            count += 1
            j = k + 1
            ans = 0
    if count == n:
        print('NO')

