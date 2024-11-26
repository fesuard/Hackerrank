# https://www.hackerrank.com/challenges/making-anagrams/problem
# Given two strings, s1 and s2, that may not be of the same length, determine the minimum
# number of character deletions required to make s1 and s2 anagrams. Any characters can be
# deleted from either of the strings. 
import math
import os
import random
import re
import sys


def makingAnagrams(s1, s2):
    hashm1 = {}
    hashm2 = {}
    res = 0
    
    for char in s1:
        hashm1[char] = hashm1.get(char, 0) + 1
    for char in s2:
        hashm2[char] = hashm2.get(char, 0) + 1
        
    for char in hashm1.keys():
        if char in hashm2:
            if hashm1[char] > hashm2[char]:
                res += hashm1[char] - hashm2[char]
        else:
            res += hashm1[char]

    for char in hashm2.keys():
        if char in hashm1:
            if hashm2[char] > hashm1[char]:
                res += hashm2[char] - hashm1[char]
        else:
            res += hashm2[char]
            
    return res
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
