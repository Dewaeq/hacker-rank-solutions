values = []

n = int(input())
values = list(map(int, input().split()))

positive = len([x for x in values if x > 0])
negative = len([x for x in values if x < 0])
zeros = len([x for x in values if x == 0])

print("{:.6f}".format(positive/n))
print("{:.6f}".format(negative/n))
print("{:.6f}".format(zeros/n))
