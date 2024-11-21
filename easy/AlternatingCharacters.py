# https://www.hackerrank.com/challenges/alternating-characters/problem
# You are given a string containing characters A and only. Your task is to change it into 
# a string such that there are no matching adjacent characters. To do this, you are allowed
# to delete zero or more characters in the string. Your task is to find the minimum number
# of required deletions.
import math
import os
import random
import re
import sys


def alternatingCharacters(s):
    res = 0
    
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            res += 1
            
    return res
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
