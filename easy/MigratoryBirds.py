# https://www.hackerrank.com/challenges/migratory-birds/problem
# Given an array of bird sightings where every element represents a bird type id, 
# determine the id of the most frequently sighted type. If more than 1 type has been 
# spotted that maximum amount, return the smallest of their ids.
import math
import os
import random
import re
import sys


def migratoryBirds(arr):
    hmap = dict()
    for no in arr:
        hmap[no] = hmap.get(no, 0) + 1
    high_keys = []
    for key, value in hmap.items():
        if value == max(hmap.values()):
            high_keys.append(key)
    return min(high_keys)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
