# https://www.hackerrank.com/challenges/two-strings/problem
# Given two strings, determine if they share a common substring. A substring may be
# as small as one character. 
import math
import os
import random
import re
import sys


def twoStrings(s1, s2):
    s1_set = set(s1)
    s2_set = set(s2)
    s = s1_set - s2_set
    
    if len(s1_set) == len(s):
        return 'NO'
    else:
        return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
