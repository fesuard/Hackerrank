# https://www.hackerrank.com/challenges/beautiful-triplets/problem
# Given a sequence of integers a, a triplet (a[i], a[j], a[k]) is beautiful if:
# i < j < k
# a[j] - a[i] = a[k] - a[j]
# Given an increasing sequenc of integers and the value of d, count the number 
# of beautiful triplets in the sequence.
import math
import os
import random
import re
import sys


def beautifulTriplets(d, arr):
    res = 0    
    
    for num in arr:
        if num + d in arr and num + 2 * d in arr:
            res += 1
    
    return res
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
