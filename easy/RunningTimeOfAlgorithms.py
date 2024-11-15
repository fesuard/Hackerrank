# https://www.hackerrank.com/challenges/runningtime/problem
# For an insertion sort algorithm, return the total number of steps needed to be done
# so that the list is sorted.
import math
import os
import random
import re
import sys


def runningTime(arr):
    res = 0
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        
        while j > 0 and arr[j-1] > key:
            res += 1
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = key
        
    return res
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
