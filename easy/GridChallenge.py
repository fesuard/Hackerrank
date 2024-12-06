# https://www.hackerrank.com/challenges/grid-challenge/problem
# Given a square grid of characters in the range ascii[a-z], rearrange elements of 
# each row alphabetically, ascending. Determine if the columns are also in ascending 
# alphabetical order, top to bottom. Return YES if they are or NO if they are not.
import math
import os
import random
import re
import sys


def gridChallenge(grid):
    for i in range(len(grid)):
        lst = sorted(grid[i])
        grid[i] = ''.join(lst)
    
    for i in range(len(grid) - 1):
        for j in range(len(grid[0])):
            if ord(grid[i][j]) > ord(grid[i+1][j]):
                return 'NO'
                
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
