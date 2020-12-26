
s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())

apples = list(map(int, input().split()))
oranges = list(map(int, input().split()))
h_apples = [x for x in apples if x + a in range(s,t+1)]
h_oranges = [x for x in oranges if x + b in range(s,t+1)]

print(len(h_apples))
print(len(h_oranges))
