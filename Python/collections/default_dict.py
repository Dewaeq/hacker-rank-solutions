from collections import defaultdict

n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]

d = defaultdict(list)

for i, val in enumerate(a):
    d[val].append(a.index(val, i) +1)
for x in b:
    if x not in a:
        print(-1)
    else:
        print(" ".join(map(str, d[x])))