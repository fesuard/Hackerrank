# https://www.hackerrank.com/challenges/missing-numbers/problem
# Given two arrays of integers, find which elements in the second array are missing 
# from the first array. If a number occurs multiple times in the lists, you must 
# ensure that the frequency of that number in both lists is the same. If that is 
# not the case, then it is also a missing number. Return the missing numbers sorted
# ascending. Only include a missing number once, even if it is missing multiple times. 
import math
import os
import random
import re
import sys


def missingNumbers(arr, brr):
    hmap1 = {}
    hmap2 = {}
    res = []
    
    for elem in arr:
        hmap1[elem] = hmap1.get(elem, 0) + 1
    for elem in brr:
        hmap2[elem] = hmap2.get(elem, 0) + 1
        
    for elem in hmap2:
        if elem in hmap1:
            freq = hmap2[elem] - hmap1[elem]
            if freq > 0:
                res.append(elem)
        else:
            res.append(elem)
            
    return sorted(res)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
