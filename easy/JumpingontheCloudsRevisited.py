# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
# A child is playing a cloud hopping game. In this game, there are sequentially numbered clouds that can be thunderheads or 
# cumulus clouds. The character must jump from cloud to cloud until it reaches the start again. There is an array of clouds c,
# and an energy level e = 100. The character starts from c[0] and uses 1 unit of energy to make a jump of size k to cloud
# c[(i+k) % n]. If it lands on a thundercloud c[i] = 1, its energy (e) decreases by 2 additional units. The game ends when
# the character lands back on cloud 0. Given the values of n, k, and the configuration of the clouds as an array c, determine 
# the final value of e after the game ends.
import math
import os
import random
import re
import sys


def jumpingOnClouds(c, k):
    i = 0
    n = len(c)
    e = 100
    game = True
    while game:
        if i + k == n:
            i = 0
            game = False
        elif i + k > n:
            i = (i+k) % n
        else:
            i = i + k
        if c[i] == 0:
            e -= 1
        else:
            e -= 3
    return e


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
