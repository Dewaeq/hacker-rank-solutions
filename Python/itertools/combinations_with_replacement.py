from itertools import combinations_with_replacement

S, k = input().split()
k = int(k)
S = list(S)
S = sorted(S)

for com in combinations_with_replacement(S, k):
    print(''.join(com))