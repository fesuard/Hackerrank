# The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, 
# its height increases by 1 meter. A Utopian Tree sapling with a height of 1 meter is planted at the onset of 
# spring. How tall will the tree be after n growth cycles?


import math
import os
import random
import re
import sys


def utopianTree(n):
    res = 1
    for i in range(n):
        if i % 2 == 0:
            res *= 2
        else: 
            res += 1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
