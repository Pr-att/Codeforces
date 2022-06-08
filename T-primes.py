import math

num = int(input())
my_List = list(map(int, input().split()))
for _ in range(num):
    count = 0
    n = my_List[_]
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n / i == i:
                count += 1
            else:
                count += 2
    if count == 3:
        print('YES')
    else:
        print('NO')
