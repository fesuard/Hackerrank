# https://www.hackerrank.com/challenges/a-very-big-sum/problem
# In this challenge, you are required to calculate and print the sum of the elements in an array, 
# keeping in mind that some of those integers may be quite large.
# Function Description
# Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.
# aVeryBigSum has the following parameter(s):
#     int ar[n]: an array of integers .
import math
import os
import random
import re
import sys


def aVeryBigSum(ar):
    return sum(ar)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
