# https://www.hackerrank.com/challenges/anagram/problem
# Two words are anagrams of one another if their letters can be rearranged to form 
# the other word. Given a string, split it into two contiguous substrings of equal
# length. Determine the minimum number of characters to change to make the two 
# substrings into anagrams of one another.
import math
import os
import random
import re
import sys


# using remove:
def anagram(s):
    n = len(s)
    
    if n % 2 == 0:
        res = 0
        s1 = list(s[:n//2])
        s2 = list(s[n//2:])
        for i in range(len(s1)):
            if s1[i] in s2:
                s2.remove(s1[i])
        return len(s2)
    
    return -1

# using hashmap
def anagram1(s):
    n = len(s)
    
    if n % 2 == 0:
        res = 0
        s1 = s[:n//2]
        s2 = s[n//2:]
        hm1 = {}
        hm2 = {}
        
        for i in range(len(s1)):
            hm1[s1[i]] = hm1.get(s1[i], 0) + 1
            hm2[s2[i]] = hm2.get(s2[i], 0) + 1
        
        for key in hm1.keys():
            if key in hm2:
                if hm1[key] > hm2[key]:
                    res += hm1[key] - hm2[key]
            else:
                res += hm1[key]
                
        return res
        
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
