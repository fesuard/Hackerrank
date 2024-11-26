# https://www.hackerrank.com/challenges/game-of-thrones/problem
# To lock the door he needs a key that is an anagram of a palindrome. He starts to go 
# through his box of strings, checking to see if they can be rearranged into a palindrome. 
# Given a string, determine if it can be rearranged into a palindrome. Return the string 
# YES or NO. 
import math
import os
import random
import re
import sys


def gameOfThrones(s):
    hashm = {}
    
    for char in s:
        hashm[char] = hashm.get(char, 0) + 1
        
    if len(s) % 2 == 0:
        if all(int(x) % 2 == 0 for x in hashm.values()):
            return 'YES'
        else:
            return 'NO'
    
    else:
        odd = 0
        for num in hashm.values():
            if num % 2 != 0:
                odd += 1
        if odd == 1:
            return 'YES'
        else:
            return 'NO'
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
