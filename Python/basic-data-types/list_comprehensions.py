x, y, z, n = (int(input()) for _ in range(4))

'''
i + j + k != n

0 =< i =< x
0 =< j =< y
0 =< k =< z


l = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i + j + k != 3:
                l.append([i, j, k])
print(l)
'''

print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n])