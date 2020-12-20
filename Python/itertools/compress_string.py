from itertools import groupby

S = input()
S = list(S)

for key, group in groupby(S):
    n = len(list(group)), int(key)
    print(tuple(n), end=" ")

