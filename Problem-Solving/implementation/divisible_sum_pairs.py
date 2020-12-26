from itertools import combinations

n, k = map(int, input().split())
ar = list(map(int, input().split()))

pairs = [x for x in list(combinations(ar, 2)) if sum(x) % k == 0]
print(len(pairs))
