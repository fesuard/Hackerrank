# https://www.hackerrank.com/challenges/weighted-uniform-string/problem
# A weighted string is a string of lowercase English letters where each letter has a weight.
# Character weights are 1 to 26 from A to Z. The weight of a string is the sum of the weights
# of its characters. A uniform string consists of a single character repeated zero or more times.
# For example, ccc and a are uniform strings, but bcb and cd are not. Given a string s, let U be 
# the set of weights for all possible uniform contiguous substrings of string s. There will be n
# queries to answer where each query consists of a single integer. Create a return array where
# for each query, the value is Yes if query[i] is in U. Otherwise, append No.
import math
import os
import random
import re
import sys


def weightedUniformStrings(s, queries):
    weights = []
    hashm = {}
    alpha = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
        'w', 'x', 'y', 'z'
    ]
    nums = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
        17, 18, 19, 20, 21, 22, 23, 24, 25, 26
    ]
    
    for i in range(len(alpha)):
        hashm[alpha[i]] = nums[i]
    
    check = []
    weight = 0
  
    for i in range(len(s)):
        if s[i] in check:
            weight += hashm[s[i]]
            weights.append(weight)
          
        else:
            if check:
                check.pop()
            check.append(s[i])
            weight = hashm[s[i]]
            weights.append(weight)
            
    return ['Yes' if q in weights else 'No' for q in queries]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
