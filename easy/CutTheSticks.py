# https://www.hackerrank.com/challenges/cut-the-sticks/problem
# You are given a number of sticks of varying lengths. You will iteratively cut the sticks into smaller sticks, 
# discarding the shortest pieces until there are none left. At each iteration you will determine the length of 
# the shortest stick remaining, cut that length from each of the longer sticks and then discard all the pieces 
# of that shortest length. When all the remaining sticks are the same length, they cannot be shortened so 
# discard them. Given the lengths of n sticks, print the number of sticks that are left before each iteration
# until there are none left.
import math
import os
import random
import re
import sys


# using count
def cutTheSticks(arr):
    n = len(arr)
    srt = sorted(list(set(arr)))
    res = [n]
    for no in srt:
        n -= arr.count(no)
        res.append(n)
    return res[:-1]

# hashmap
def cutTheSticks1(arr):
    hashm = {}
    n = len(arr)
    res = [n]
    for elem in arr:
        hashm[elem] = hashm.get(elem, 0) + 1
    keys = sorted(hashm.keys())
    for key in keys:
        n -= hashm[key]
        res.append(n)
    return res[:-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
