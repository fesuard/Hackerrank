# You must distribute loathes of bread evenly, following these rules:
#   1.Every time you give a loaf of bread to some person i, you must also give a loaf of bread 
#   to the person immediately in front of or behind them in the line (i.e., persons i+1 or i-1). 
#   2.After all the bread is distributed, each person must have an even number of loaves.
# Given the number of loaves already held by each citizen, find and print the minimum number of 
# loaves you must distribute to satisfy the two rules above. If this is not possible, print NO.
import math
import os
import random
import re
import sys


def fairRations(B):
    n = len(B)
    res = 0
    
    for i in range(n-1):
        if B[i] % 2 != 0:
            B[i+1] += 1
            res += 2
    
    if B[-1] % 2 == 0:
        return str(res)
    
    if B[-1] % 2 != 0:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(result + '\n')

    fptr.close()
