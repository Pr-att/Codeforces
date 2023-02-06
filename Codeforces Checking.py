from collections import defaultdict

d = defaultdict(lambda: "NO")
for k in "codeforces":
    d[k] = 'YES'

for idx in range(int(input())):
    word = input()
    print(d[word])