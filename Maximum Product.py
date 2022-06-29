for _ in range(int(input())):
    num = int(input())
    array = sorted(list(map(int, input().split())))
    # print(array)
    first_two = array[0] * array[1] * array[-1] * array[-2] * array[-3]
    first_four = array[0] * array[1] * array[2] * array[3] * array[-1]
    last_two = array[-1] * array[-2] * array[0] * array[1] * array[2]
    last_four = array[-1] * array[-2] * array[-3] * array[-4] * array[0]
    first_five = array[0] * array[1] * array[2] * array[3] * array[4]
    last_five = array[-1] * array[-2] * array[-3] * array[-4] * array[-5]
    # print(first_two, first_four, last_two, last_four)
    ans = max(first_two, first_four, last_two, last_four, first_five, last_five)
    print(ans)
