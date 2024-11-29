# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
# Given an array of integers, find the minimum absolute difference between any two
# elements in the array. 
import math
import os
import random
import re
import sys


def minimumAbsoluteDifference(arr):
    arr.sort()
    res = []
    
    for i in range(len(arr) - 1):
        res.append(abs(arr[i] - arr[i+1]))
    
    return min(res)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
