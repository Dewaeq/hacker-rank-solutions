#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    if n == 0:
        return 1

    f = n
    n -= 1

    while n > 0:
        f *= n
        n -= 1

    print(f)

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)

