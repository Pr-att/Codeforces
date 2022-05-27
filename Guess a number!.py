# TODO: Not Completed.

p1, p2 = 0, 0
for i in range(int(input())):
    statement = input().split()
    if statement[2] == 'N':
        if statement[0] == '>=':
            statement[0] = '<'
        elif statement[0] == '>':
            statement[0] = '<='
        elif statement[0] == '<=':
            statement[0] = '>'
        elif statement[0] == '<':
            statement[0] = '>='

    if statement[0] == '>=' and int(statement[1]) >= p1:
        p1 = int(statement[1])
    elif statement[0] == '>' and int(statement[1]) >= p1:
        pass

    # if statement[2] == 'Y':
    #     if statement[0] == '>=' and int(statement[1]) >= p1:
    #         p1 = int(statement[1])
    #     elif statement[0] == '>' and int(statement[1]) >= p1:
    #         p1 = int(statement[1]) + 1
    #     elif statement[0] == '<=':
    #         p2 = int(statement[1])
    #     elif statement[0] == '<':
    #         p2 = int(statement[1]) - 1


print(p1, p2)
