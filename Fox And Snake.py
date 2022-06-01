def solve(a, b):
    body = "#"
    snake_bodies = body * b
    empty = "." * (b - 1)
    my_bool = True

    for row in range(0, a):

        if row % 2 == 0:
            print(snake_bodies)
        else:
            if my_bool:
                print(empty + body)
            else:
                print(body + empty)
            my_bool = not my_bool


n, m = map(int, input().split())
solve(n, m)
