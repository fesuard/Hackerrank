# https://www.hackerrank.com/challenges/maximizing-xor/problem
# Given two integers, l and r, find the maximal value of a XOR b, written as a ⊕ b, where a and b satisfy the following condition:
# l ≤ a ≤ b ≤ r
# For example, if l = 11 and r = 12, then:
# 11 ⊕ 11 = 0
# 11 ⊕ 12 = 7
# 12 ⊕ 12 = 0
# Our maximum value is 7.
import math
import os
import random
import re
import sys


def maximizingXor(l, r):
    xor = 0
    
    for i in range(l, r + 1):
        for j in range(i, r + 1):
            xor = max(xor, i ^ j)
            
    return xor


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
