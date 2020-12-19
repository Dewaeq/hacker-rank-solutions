from itertools import combinations

letters, n = input().split()
n = int(n)
letters = sorted(letters)

l = []
for i in range(1,n+1):
    temp = []
    for j in combinations(letters, i):
        temp.append(''.join(j))
    l.extend(sorted(temp))
    
for words in l:
    print(words)