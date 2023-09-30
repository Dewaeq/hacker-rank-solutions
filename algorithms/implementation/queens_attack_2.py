#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    diagonal = r_q - c_q;
    anti_diagonal = r_q + c_q;

    obstacles = list(filter(lambda o: o[0] == r_q or o[1] == c_q or (o[0] - o[1] == diagonal) or (o[0] + o[1] == anti_diagonal), obstacles))

    c = 0
    sq = (r_q, c_q)
    for d in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
        s = sq
        while True:
            s = tuple(map(sum, zip(s, d)))
            if s in obstacles or s[0] > n or s[1] > n or s[0] < 1 or s[1] < 1:
                break
            c += 1

    print(c)

if __name__ == '__main__':
    #    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(tuple(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

#    fptr.write(str(result) + '\n')
#
#    fptr.close()

