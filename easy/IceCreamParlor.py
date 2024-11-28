# https://www.hackerrank.com/challenges/icecream-parlor/problem
# Two friends like to pool their money and go to the ice cream parlor. They always choose
# two distinct flavors and they spend all of their money. Given a list of prices for the
# flavors of ice cream, select the two that will cost all of the money they have. 
import math
import os
import random
import re
import sys


def icecreamParlor(m, arr):
    res = []
    
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == m:
                res.extend([i + 1, j + 1])
    
    res.sort()
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
