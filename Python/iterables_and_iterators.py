from itertools import combinations

N = int(input())                    # Length of list
letters = input().split()           # N letters (= the list)
K = int(input())                    # Number of indices to select

c = 0
coms = list(combinations(letters, K))
for i in coms:
    if 'a' in i:
        c = c + 1
print("{:.3f}".format(c/len(coms)))