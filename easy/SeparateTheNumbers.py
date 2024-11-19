# https://www.hackerrank.com/challenges/separate-the-numbers/problem
# A numeric string s, is beautiful if it can be split into a sequence of two or more
# positive integers, a[1], a[2],..., a[n] satisfying the following conditions:
# 1. each element in the sequence is 1 more than the previous element
# 2. No a[i] contains a leading zero.
# 3. The contents of the sequence cannot be rearranged, for example {3, 1, 2} cannot
# be considered beautiful.
import math
import os
import random
import re
import sys


def separateNumbers(s):
    n = len(s)
    res = [False, 0]
    
    for i in range(1, n // 2 + 1):
        new_str = s[:i]
        num = int(s[:i])
        
        while len(new_str) < n:
            new_str += str(num + 1)
            num += 1
        
        if s == new_str:
            res[0] = True
            res[1] = int(s[:i])
            break
    
    if res[0]:
        print(f'YES {res[1]}')
    else:
        print('NO')
            

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
