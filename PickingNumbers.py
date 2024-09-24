# Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1. 

import math
import os
import random
import re
import sys


def pickingNumbers(a):
    hashm = {}
    res = 0
    for no in a:
        hashm[no] = hashm.get(no, 0) + 1
    res = max(hashm[key] + hashm.get(key+1, 0) for key in hashm.keys())
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
