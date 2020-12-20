n = int(input())
A = map(int, input().split())
A = sorted(A, reverse=True)
a_max = max(A)

for a in A:
    if a < a_max:
        print(a)
        break

'''
Alternate solution

n = input()
a = map(int, input().split())
a = list(set(a))
a.remove(max(a))
print(max(a))
'''