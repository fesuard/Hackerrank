# https://www.hackerrank.com/challenges/diagonal-difference/problem
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# For example, the square matrix arr is shown below:
import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    d1 = []
    d2 = []
    n = len(arr) - 1
    for i in range(len(arr)):
        d1.append(arr[i][i])
        d2.append(arr[i][n-i])
    return abs(sum(d1) - sum(d2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
