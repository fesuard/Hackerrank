# https://www.hackerrank.com/challenges/service-lane/problem
# You will be given an array of widths at points along the road (indices), then a list 
# of the indices of entry and exit points. Considering each entry and exit point pair, 
# calculate the maximum size vehicle that can travel that segment of the service lane
# safely.
import math
import os
import random
import re
import sys


def serviceLane(width, cases):
    res = []
    
    for case in cases:
        res.append(min(width[case[0] : case[1] + 1]))
        
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(width, cases)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
