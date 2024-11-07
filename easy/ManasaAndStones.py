# https://www.hackerrank.com/challenges/manasa-and-stones/problem
# Manasa is out on a hike with friends. She finds a trail of stones with numbers on them. 
# She starts following the trail and notices that any two consecutive stones' numbers differ 
# by one of two values. Legend has it that there is a treasure trove at the end of the trail. 
# If Manasa can guess the value of the last stone, the treasure will be hers. Tell her what
# can the possible values be for the last stone.
import math
import os
import random
import re
import sys


def stones(n, a, b):
    res = set()
    
    for i in range(n):
        res.add(a * (n-i-1) + b * i)
    
    return sorted(res)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        a = int(input().strip())

        b = int(input().strip())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
