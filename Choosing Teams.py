n, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
count, i = 0, 0
while i != n - 2:
    try:
        if nums[i + 2] + k <= 5:
            count += 1
            i += 3
        else:
            break
    except IndexError:
        break
print(count)
