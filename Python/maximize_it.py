from itertools import product

n,m = [int(x) for x in input().split()]
L = list()

for i in range(n):
    l = list(map(int, input().split()))[1:]
    L.append(l)

r = map(lambda x: sum(i*i for i in x) % m, product(*L))
print(max(r))

'''
(K, N) = map(int, input().strip().split(' '))

# reading the K lines and appending lists to 'L'
L = list()
for i in range(K):
    l = list(map(int, input().strip().split(' ')))
    n = l[0]
    L.append(l[1:])
    assert(len(L[i])) == n

S_max = 0
L_max = None

# Looping through Cartesian product of list and getting max sum
for l in product(*L):
    s = sum([x**2 for x in l]) % N

    if s > S_max:
        S_max = s
        L_max = 1
'''