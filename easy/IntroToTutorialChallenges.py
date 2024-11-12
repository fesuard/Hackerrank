# Complete the introTutorial function in the editor below. It must return an integer 
# representing the zero-based index of V.
# introTutorial has the following parameter(s):
#     int arr[n]: a sorted array of integers
#     int V: an integer to search for
# Returns
#     int: the index of V in arr
import math
import os
import random
import re
import sys


def introTutorial(V, arr):
    return arr.index(V)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input().strip())

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
