n = int(input())
scores = list(map(int, input().split()))

cb, cw = 0, 0

for i in range(1,n):
    if scores[i] > max(scores[:i]):
        cb += 1

    if scores[i] < min(scores[:i]):
        cw += 1
print(cb, cw)
