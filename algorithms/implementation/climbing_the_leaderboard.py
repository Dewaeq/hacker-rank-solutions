#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def climbingLeaderboard(ranked, player):
    r = []
    scores = list(sorted(set(ranked), reverse=True))
    n = len(scores)

    i = 0
    for score in player:
        while i < n and scores[n - i - 1] <= score:
            i += 1
        r.append(n - i + 1)

    return r


if __name__ == '__main__':
    result = climbingLeaderboard(
        [100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120])

    print(result)
