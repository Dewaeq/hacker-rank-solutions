from collections import Counter

n = int(input())
ar = list(map(int, input().split()))

c = Counter(ar)
m = max(c.values())

res = [x for x in c.keys() if c[x] == m]

print(min(res))