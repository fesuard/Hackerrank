# https://www.hackerrank.com/challenges/kaprekar-numbers/problem
# Consider a positive whole number n with digits d. We square n to arrive at a number that is 
# either (2 x d) digits long or (2 x d) - 1 digits long. Split the string representation of 
# the square into two parts, l and r. The right hand part r, must be d digits long. The left
# is the remaining substring. Convert those two substrings back to integers, add them and see
# if you get n.
import math
import os
import random
import re
import sys


def kaprekarNumbers(p, q):
    res = []
    
    for num in range(p, q + 1):
        n = len(str(num))
        m = len(str(num ** 2))
        
        if num == 1:
            res.append(str(num))
        
        if m == 2 * n or m == 2 * n - 1 and m - n > 0:
            sq = num ** 2
            if int(str(sq)[:-n]) + int(str(sq)[-n:]) == num:
                res.append(str(num))
            
    if res:
        print(' '.join(res))
    else:
        print('INVALID RANGE')
        
        
if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
