# There is a string s, of lowercase English letters that is repeated infinitely many times. Given an
# integer n, find and print the number of letter a's in the first letters of the infinite string.
import math
import os
import random
import re
import sys


def repeatedString(s, n):
    count = 0
    ls = len(s)
            
    if n < ls:
        return s[:n].count('a')
    
    for char in s:
        if char == 'a':
            count += 1
            
    repeat = n // ls
    remainder = n % ls
    count *= repeat
    count += s[:remainder].count('a')
    
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
