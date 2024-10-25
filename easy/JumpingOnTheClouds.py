# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
# There are a number of clouds, some of the clouds are thunderheads and others are cumulus.
# The player can jump on any cumulus cloud having a number that is equal to the number of the
# current cloud plus 1 or plus 2. The player must avoid the thunderheads. Determine the minimum
# number of jumps it will take to jump from the starting postion to the last cloud. It is always 
# possible to win the game. For each game, you will get an array of clouds numbered if they are 
# safe or if they must be avoided. 
#!/bin/python3
import math
import os
import random
import re
import sys


def jumpingOnClouds(c):
    res = 0
    n = len(c)
    
    if n <= 3:
        return 1
    
    i = 0
    j = 1
    
    while i < n - 2:
        if c[i+2] == 0:
            i += 2
        else:
            i += 1
        res += 1
        
    if i != n - 1:
        res += 1
        
    return res
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
