# https://www.hackerrank.com/challenges/find-the-median/problem
# The median of a list of numbers is essentially its middle element after sorting. The
# same number of elements occur after it as before. Given a list of numbers with an odd
# number of elements, find the median?
import math
import os
import random
import re
import sys


def findMedian(arr):
    arr.sort()
    mid = len(arr) // 2
    return arr[mid]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
