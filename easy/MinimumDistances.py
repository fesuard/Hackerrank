# https://www.hackerrank.com/challenges/minimum-distances/problem
# The distance between two array values is the number of indices between them. Given a, find the minimum 
# distance between any pair of equal elements in the array. If no such value exists, return -1.
import math
import os
import random
import re
import sys


def minimumDistances(a):
    indexes = {}
    res = []

    for i, val in enumerate(a):
        if val in indexes:
            res.append(i - indexes[val])
            indexes[val] = i
        else:
            indexes[val] = i
            
    if res:
        return min(res)
    else:
        return -1
        
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
