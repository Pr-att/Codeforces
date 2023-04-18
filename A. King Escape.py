import sys

sys.setrecursionlimit(1000000)


def dfs(i, j, p, q, Set, found):
    if found:
        return
    if Set[i][j] == 1:
        return
    Set[i][j] = 1
    if i < 0 or i >= p - 1 or j < 0 or j >= q - 1:
        return
    if i == e - 1 and j == f - 1:
        found = True
        return
    else:
        dfs(i + 1, j, p, q, Set, found)
        dfs(i - 1, j, p, q, Set, found)
        dfs(i, j + 1, p, q, Set, found)
        dfs(i, j - 1, p, q, Set, found)
        dfs(i + 1, j + 1, p, q, Set, found)
        dfs(i - 1, j - 1, p, q, Set, found)
        dfs(i + 1, j - 1, p, q, Set, found)
        dfs(i - 1, j + 1, p, q, Set, found)


n = int(input())
a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

visited = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(0, n):
    visited[_][a - 1] = 1  # Horizontal
for _ in range(0, n):
    visited[b - 1][_] = 1  # Vertical

# Diagonals
for _ in range(abs(a - b), min(a, b)):
    visited[_][abs(a - b) + _] = 1
for _ in range(min(a, b), a + b):
    visited[_][abs(a - b) + _] = 1
for _ in range(0, min(a, b)):
    visited[_][(a - 1 + b - 1) - _] = 1
for _ in range(min(a, b), a + b):
    visited[_][(a - 1 + b - 1) - _] = 1

found = False
dfs(c - 1, d - 1, n, n, visited, found)
if found:
    print("YES")
else:
    print("NO")

# Trash Question for DFS
