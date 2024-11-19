# In this challenge, you will determine whether a string is funny or not. To determine
# whether a string is funny, create a copy of the string in reverse e.g. Iterating 
# through each string, compare the absolute difference in the ascii values of the
# characters at positions 0 and 1, 1 and 2 and so on to the end. If the list of
# absolute differences is the same for both strings, they are funny.Determine whether
# a give string is funny. If it is, return Funny, otherwise return Not Funny.
import math
import os
import random
import re
import sys


def funnyString(s):
    reverse_s = s[::-1]
    
    for i in range(len(s) - 1):
        dif1 = abs(ord(s[i]) - ord(s[i+1]))
        dif2 = abs(ord(reverse_s[i]) - ord(reverse_s[i+1]))
        if dif1 != dif2:
            return 'Not Funny'
    
    return 'Funny'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
