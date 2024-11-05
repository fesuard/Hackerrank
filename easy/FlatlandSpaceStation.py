# Flatland is a country with a number of cities, some of which have space stations. Cities
# are numbered consecutively and each has a road of length connecting it to the next city.
# It is not a circular route, so the first city doesn't connect with the last city. Determine
# the maximum distance from any city to its nearest space station.
import math
import os
import random
import re
import sys


def flatlandSpaceStations(n, c):
    if n == m:
        return 0
    res = 0
    
    for i in range(n):
        temp = min(abs(i-j) for j in c)
        if temp > res:
            res = temp
    
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
