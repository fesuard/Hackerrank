# https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem
# You are given the total number of digits of an integer value. Find the biggest
# number you can form, given the following rules for valid numbers:
#   Its digits can only be 3's and/or 5's.
#   The number of 3's it contains is divisible by 5.
#   The number of 5's it contains is divisible by 3.
#   It is the largest such number for its length.
# If you can't find any numbers, return -1.
import math
import os
import random
import re
import sys


def decentNumber(n):
    if n < 3:
        return -1
        
    if n % 3 == 0:
        return '5' * n
    
    divisible_lengths_by_3 = [x for x in range(n, 2, -1) if x % 3 == 0]
    divisible_lengths_by_5 = [x for x in range(5, n + 1) if x % 5 == 0]
    
    
    for a in divisible_lengths_by_3:
        for b in divisible_lengths_by_5:
            if a + b == n:
                return '5' * a + '3' * b
                
    if n % 5 == 0:
        return '3' * n
        
    return -1
    
    
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        print(decentNumber(n))
