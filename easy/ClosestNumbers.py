# https://www.hackerrank.com/challenges/closest-numbers/problem
# Given a list of unsorted integers arr, find the pair of elements that have the smallest 
# absolute difference between them. If there are multiple pairs, find them all.
# Returns
# - int[]: an array of integers as described 
import math
import os
import random
import re
import sys


def closestNumbers(arr):
    res = []
    arr.sort()
    diff = []
    pair_arr = list(zip(arr, arr[1:]))
    
    for elem in pair_arr:
        diff.append(elem[1] - elem[0])
    
    min_diff = min(diff)
    for elem in pair_arr:
        if elem[1] - elem[0] == min_diff:
            res.extend([*elem])
    
    return res
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
