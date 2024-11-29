# https://www.hackerrank.com/challenges/sherlock-and-array/problem
# Watson gives Sherlock an array of integers. His challenge is to find an element of the
# array such that the sum of all elements to the left is equal to the sum of all elements
# to the right.
import math
import os
import random
import re
import sys


# brute force
def balancedSums(arr):
    if len(arr) == 1:
        return 'YES'
    
    if sum(arr[1:]) == 0 or sum(arr[:-1]) == 0:
        return 'YES'
        
    for i in range(1, len(arr) - 1):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return 'YES'
            
    return 'NO'

# more efficient method using the total sum
def balancedSums1(arr):
    left_sum = 0
    total_sum = sum(arr)
    
    for elem in arr:
        right_sum = total_sum - left_sum - elem
        if left_sum == right_sum:
            return 'YES'
        left_sum += elem
            
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
