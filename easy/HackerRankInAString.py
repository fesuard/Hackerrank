# https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
# We say that a string contains the word hackerrank if a subsequence of its characters 
# spell the word hackerrank. Remeber that a subsequence maintains the order of characters 
# selected from a sequence. More formally, let p[0], p[1], ... , p[9] be the respective
# indices of h, a, c, k, e, r, r, a, n, k in string s. If p[0] < p[1] < ... < p[9] is true,
# then s contains hackerrank. For each query, print YES on a new line if the string contains 
# hackerrank, otherwise, print NO. 
import math
import os
import random
import re
import sys


def hackerrankInString(s):
    hacker = 'hackerrank'
    j = 0
    correct = True
    
    for i in range(len(hacker)):
        while j < len(s) and hacker[i] != s[j]:
            j += 1
        if j == len(s):
            correct = False
            break
        j += 1
        
    if correct:
        return 'YES'
    else:
        return 'NO'
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
