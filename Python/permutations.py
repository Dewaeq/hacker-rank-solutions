from itertools import permutations

'''
Task

You are given a string .
Your task is to print all possible permutations of size of the string in lexicographic sorted order.
'''
inp = input().split()
S = inp[0]
k = int(inp[1])
sList = [char for char in S]

rList = []
for i in permutations(sList, k):
    result = ""
    for x in i:
        result = result + x
    rList.append(result)

rList = sorted(rList)
for i in rList:
    print(i)
