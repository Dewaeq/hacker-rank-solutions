x1, v1, x2, v2 = map(int, input().split())

pos1 = x1
pos2 = x2

if x1 < x2 and v1 < v2 or x1 > x2 and v1 > v2:
    print("NO")

else:
    if v2 - v1 == 0 and x1 != x2:
        print("NO")
    elif (x2-x1) % (v2-v1) == 0:
        print("YES")
    else:
        print("NO")

