# Reduce a string of lowercase characters in range ascii[‘a’..’z’]by doing a series of
# operations. In each operation, select a pair of adjacent letters that match, and delete
# them. Delete as many characters as possible using this method and return the resulting 
# string. If the final string is empty, return Empty String
import math
import os
import random
import re
import sys


def superReducedString(s):
    res = []
    
    for i in range(len(s)):
        if len(res) == 0 or s[i] != res[-1]:
            res.append(s[i])
        else:
            res.pop()
            
    if res:
        return ''.join(res)
    else:
        return 'Empty String'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
