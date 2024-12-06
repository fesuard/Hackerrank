# https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem
# Given an array of stick lengths, use 3 of them to construct a non-degenerate triangle
# with the maximum possible perimeter. Return an array of the lengths of its sides as 3
# integers in non-decreasing order.
# If there are several valid triangles having the maximum perimeter:
# Choose the one with the longest maximum side.
# If more than one has that maximum, choose from them the one with the longest minimum
# side.
# If more than one has that maximum as well, print any one them.
# If no non-degenerate triangle exists, return [-1].
import math
import os
import random
import re
import sys


def maximumPerimeterTriangle(sticks):
    n = len(sticks)
    sticks.sort()
    
    for i in range(n-1, 1, -1):
        if sticks[i] < sticks[i-1] + sticks[i-2]:
            return [sticks[i-2], sticks[i-1], sticks[i]]
    
    return [-1]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
