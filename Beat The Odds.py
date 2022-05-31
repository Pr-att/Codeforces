for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    even = 0
    odd = 0
    for i in nums:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    print(min(even, odd))

    # ans = 0
    # count = 0
    # i = 0
    # while i != n:
    #     try:
    #         if (nums[i] + nums[i + 1]) % 2 == 0:
    #             i += 1
    #             pass
    #         else:
    #             nums.pop(i + 1)
    #             i -= 1
    #             count += 1
    #     except IndexError:
    #         break
    #
    # print(count)
