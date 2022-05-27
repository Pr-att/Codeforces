a = int(input())
b = int(input())
c = int(input())
p = [a, b, c]
n1 = p[0] + p[1] + p[2]
n2 = (p[0] * p[1]) + p[2]
n3 = p[0] * p[1] * p[2]
n4 = (p[0] + p[1]) * p[2]
n5 = p[0] * (p[1] + p[2])
n6 = p[0] + (p[1] * p[2])
print(max(n1, n2, n3, n4, n5, n6))
