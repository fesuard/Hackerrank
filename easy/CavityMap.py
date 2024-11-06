# https://www.hackerrank.com/challenges/cavity-map/problem
# You are given a square map as a matrix of integer strings. Each cell of the map has a 
# value denoting its depth. We will call a cell of the map a cavity if and only if this
# cell is not on the border of the map and each cell adjacent to it has strictly smaller 
# depth. Two cells are adjacent if they have a common side, or edge.Find all the cavities
# on the map and replace their depths with the uppercase character X. 
import math
import os
import random
import re
import sys


def cavityMap(grid):
    res_grid = grid[:]
    
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid) - 1):
            cell = grid[i][j]
            
            if (cell > grid[i-1][j] and 
                cell > grid[i+1][j] and
                cell > grid[i][j+1] and
                cell > grid[i][j-1]):
                res_grid[i] = res_grid[i][:j] + 'X' + res_grid[i][j+1:]
                
    return res_grid
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()
