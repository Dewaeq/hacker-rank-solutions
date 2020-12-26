from itertools import combinations

a = list(map(int, input().split()))
coms = list(combinations(a, 4))

sums = []

for x in coms:
    sums.append(sum(x))

print(" ".join(map(str, [min(sums), max(sums)])))
