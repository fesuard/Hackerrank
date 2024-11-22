# https://www.hackerrank.com/challenges/the-love-letter-mystery/problem
# You have to change all the words into palindromes.
# To do this, he follows two rules:
#     You can only reduce the value of a letter by 1 i.e. he can change d to c, but 
# he cannot change c to d or d to b.
#     The letter a may not be reduced any further.
# Each reduction in the value of any letter is counted as a single operation. Find 
# the minimum number of operations required to convert a given string into a palindrome.
import math
import os
import random
import re
import sys


def theLoveLetterMystery(s):
    res = 0  
    i = 0
    j = len(s) - 1
    
    while i < j:
        res += abs(ord(s[i]) - ord(s[j]))
        i += 1
        j -= 1
            
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
