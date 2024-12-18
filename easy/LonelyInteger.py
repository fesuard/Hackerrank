# https://www.hackerrank.com/challenges/lonely-integer/problem
# Given an array of integers, where all elements but one occur twice, find the 
# unique element.
import math
import os
import random
import re
import sys


def lonelyinteger(a):
    hashm = {}
    
    for elem in a:
        hashm[elem] = hashm.get(elem, 0) + 1
        
    for key, val in hashm.items():
        if val == 1:
            return key


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
