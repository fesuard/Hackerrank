# https://www.hackerrank.com/challenges/sock-merchant/problem
# There is a large pile of socks that must be paired by color. Given an array of integers representing 
# the color of each sock, determine how many pairs of socks with matching colors there are.
import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    hmap = dict()
    res = 0
    for no in ar:
        hmap[no] = hmap.get(no, 0) + 1
    for value in hmap.values():
        if value >= 2:
            res += value//2
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
