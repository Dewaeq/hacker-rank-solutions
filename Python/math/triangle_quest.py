# More than 2 lines will result in 0 score. Do not leave a blank line also

for i in range(1, int(input())):
    print((10**i)//9*i)

'''
10 // 9 = 1
100 // 9 = 11
1000 // 9 = 111
'''

'''
Wrong for some unknown reason

for i in range(1, int(input())):
    print("{0}".format(i) * i)
'''