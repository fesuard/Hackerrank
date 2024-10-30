# https://www.hackerrank.com/challenges/halloween-sale/problem
# You want to buy as many games as you can. You have a total sum of s dolars, first game
# is sold for p, and every subsequent game will cost p - d, until p is capped out at m, 
# after which each game will cost m. How many games can you buy?
import math
import os
import random
import re
import sys


def howManyGames(p, d, m, s):
    res = 0
    
    while s > 0:
        if s - p >= 0:
            s -= p
            res += 1
        else:
            break
        if p - d > m:
            p -= d
        else:
            p = m
            
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
  
