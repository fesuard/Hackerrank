# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
# Given a range of numbered days [i...j], and a number k, determine the number of days in the range that are beautiful. 
# Beautiful numbers are defined as numbers where i-reverse(i) is evenly divisible by k. If a day's value is a beautiful number, 
# it is a beautiful day. Return the number of beautiful days in the range.

import math
import os
import random
import re
import sys


def beautifulDays(i, j, k):
    res = 0
    for day in range(i, j+1):
        btf = day - int(str(day)[::-1])
        if btf % k == 0:
            res += 1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
