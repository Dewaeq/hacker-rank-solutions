from collections import OrderedDict

n = int(input())
d = OrderedDict()
for i in range(n):
    item, space, price = input().rpartition(' ')
    if item in d.keys():
        d[item] += int(price)
    else:
        d[item] = int(price)

for item in d.keys():
    print(item, d[item])
