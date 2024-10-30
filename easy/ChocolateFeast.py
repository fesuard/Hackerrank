# https://www.hackerrank.com/challenges/chocolate-feast/problem
# They are having a promotion at a store. If Bobby saves enough wrappers, he can turn them in 
# for a free chocolate. Example, if you have 15 to spend, chocolates costs 4, and you get a 
# chocolate free for 3 wrappers, you buy 3, and exchange the 3 wrappers for another chocolate,
# so you eat a total of 4. How many chocolates can he eat?
import math
import os
import random
import re
import sys


def chocolateFeast(n, c, m):
    res = n // c
    wrappers = n // c
    
    while wrappers >= m:
        temp = wrappers // m
        res += temp
        wrappers -= temp * m
        wrappers += temp
        
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
