# https://www.hackerrank.com/challenges/lisa-workbook/problem
# Lisa just got a new math workbook. A workbook contains exercise problems, grouped into chapters.
# Lisa believes a problem to be special if its index (within a chapter) is the same as the page number
# where it's located. The format of Lisa's book is as follows:
# There are n chapters in Lisa's workbook, numbered from to 1 to n.
# The ith chapter has arr[i] problems, numbered from 1 to arr[i].
# Each page can hold up to k problems. Only a chapter's last page of exercises may contain fewer than k
# problems.
# Each new chapter starts on a new page, so a page will never contain problems from more than one chapter.
# The page number indexing starts at 1
# Given the details for Lisa's workbook, can you count its number of special problems?
import math
import os
import random
import re
import sys


def workbook(n, k, arr):
    res = 0
    i = 1
    j = 0
    
    for j in range(n):
        for m in range(1, arr[j] + 1):
            if m == i:
                res += 1
            if m % k == 0 and m != arr[j]:
                i += 1
        i += 1
            
    return res
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
