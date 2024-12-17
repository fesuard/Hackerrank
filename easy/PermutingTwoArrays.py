# https://www.hackerrank.com/challenges/two-arrays/problem
# There are two n-element arrays of integers, A and B. Permute them into some A' 
# and B' such that the relation A'[i] + B'[i] ≥ k holds for all i where 0 ≤ i < n.
# There will be q queries consisting of A, B, and k. For each query, return YES if 
# some permutation A' and B' satisfying the relation exists. Otherwise, return NO.
import math
import os
import random
import re
import sys


def twoArrays(k, A, B):
    asc_a = sorted(A)
    desc_b = sorted(B, reverse=True)
    
    for i in range(len(A)):
        if asc_a[i] + desc_b[i] < k:
            return 'NO'
    
    return 'YES'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
