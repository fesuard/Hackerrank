# https://www.hackerrank.com/challenges/string-construction/problem
# You are given a string s. You can perform the following operation any number 
# of times to construct the string:
#   Append a character to the end of string p at a cost of 1 dollar. 
#   Choose any substring of p and append it to the end of p at no charge.
# Given n strings, find and print the minimum cost of copying each s[i] to p[1] on 
# a new line.
import math
import os
import random
import re
import sys


def stringConstruction(s):
    return len(set(s))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
