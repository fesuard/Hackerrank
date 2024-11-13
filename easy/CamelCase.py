# There is a sequence of words in CamelCase as a string of letters shaving the 
# following properties:
#     It is a concatenation of one or more words consisting of English letters.
#     All letters in the first word are lowercase.
#     For each of the subsequent words, the first letter is uppercase and rest 
#     of the letters are lowercase.
# Given s determine the number of words in s.
import math
import os
import random
import re
import sys


def camelcase(s):
    res = 1
    
    for letter in s:
        if letter.isupper():
            res += 1
            
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
