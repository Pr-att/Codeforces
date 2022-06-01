for _ in range(1):
    n = 6
    nums = [2, 3, 4, 3, 4, 2]
    i, j = 0, 1
    array = []
    while i != n:
        try:
            if nums[j] == nums[i]:
                array.append(j + 1)
                array.append(i + 1)
            # i += 1
            j += 1

        except IndexError:
            break
    for j in array:
        print(j, end=' ')
    # hashMap, i = {}, 0
    # while i != n:
    #     if nums[i] in hashMap:
    #         hashMap[nums[i]] += 1
    #     else:
    #         hashMap[nums[i]] = 1
    #     i += 1
    # if len(hashMap.keys()) == 1:
    #     print([i + 1 for i in range(1, n + 1)])
    # elif max(hashMap.values()) > 1:
    #     for i in hashMap.values():
    #         if i == 1:
    #             print(-1)
    #             break
    #
    # for i in range(n):
    #     if nums[i] == nums[i + 1]:
    #         pass

    """
    2 2 3 3 4 4
    2 1 4 3 6 5
    
    2 3 4 3 4 2
    6 4 5 2 3 1
    
    """
