# https://www.hackerrank.com/challenges/equality-in-a-array/problem
# Given an array of integers, determine the minimum number of elements to delete to
# leave only elements of equal value.
import math
import os
import random
import re
import sys


def equalizeArray(arr):
    n = len(arr)
    hashm = {}
    
    for elem in arr:
        hashm[elem] = hashm.get(elem, 0) + 1
    
    return n - max(hashm.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
