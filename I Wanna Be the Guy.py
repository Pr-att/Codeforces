numRange = int(input())
myList = [i for i in range(1, numRange + 1)]
n1 = list(map(int, input().split()))
n2 = list(map(int, input().split()))
n3 = set(n1[1:])
n4 = set(n2[1:])
last = n3.union(n4)
if last == set(myList):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
