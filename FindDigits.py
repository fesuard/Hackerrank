# https://www.hackerrank.com/challenges/find-digits/problem
# An integer d is a divisor of an integer n if the remainder of n % d = 0. Given an integer, for each digit that makes up 
# the integer determine whether it is a divisor. Count the number of divisors occurring within the integer. 

import math
import os
import random
import re
import sys


def findDigits(n):
    res = 0
    for d in str(n):
        if int(d) != 0 and n % int(d) == 0:
            res += 1
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
