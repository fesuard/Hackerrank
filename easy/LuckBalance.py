# https://www.hackerrank.com/challenges/luck-balance/problem
# Lena is preparing for an important coding competition that is preceded by a number 
# of sequential preliminary contests. Initially, her luck balance is 0. She believes
# in "saving luck", and wants to check her theory. Each contest is described by two
# integers, L[i] and T[i]:
#   - L[i] is the amount of luck associated with a contest. If Lena wins the contest, 
# her luck balance will decrease by L[i]; if she loses it, her luck balance will 
# increase by L[i].
#   - T[i] denotes the contest's importance rating. It's equal to 1 if the contest is
# important, and it's equal to 0 if it's unimportant.
# If Lena loses no more than k important contests, what is the maximum amount of luck
# she can have after competing in all the preliminary contests? 
import math
import os
import random
import re
import sys


def luckBalance(k, contests):
    res = 0
    important = []
    unimportant = []
    
    for elem in contests:
        if elem[1] == 1:
            important.append(elem[0])
        else:
            unimportant.append(elem[0])
            
    important = sorted(important, reverse=True)
    
    if k < len(important):
        res += sum(important[:k])
        res -= sum(important[k:])
    else:
        res += sum(important)
    
    res += sum(unimportant)
    
    return res


if __name__ == '__main__':
    ftpr = open(os.environ['OUTPUT_PATH'], 'w')
    
    multiple_input1 = list(map(int, input().strip().split()))
    
    n = multiple_input1[0]
    
    k = multiple_input1[1]
    
    contests = []
    
    for _ in range(n):
        multiple_input2 = list(map(int, input().strip().split()))
        
        contests.append([multiple_input2[0], multiple_input2[1]])
        
    result = luckBalance(k, contests)
    
    ftpr.write(str(result))
    
    ftpr.close
