# https://www.hackerrank.com/challenges/permutation-equation/problem
# Given a sequence of n integers, (p(1), p(2), p(3), p(n)) where each element is distinct and 
# satisfies 1 <= p(x) <= n. For each x where 1 <= x <= n, that is x increments from 1 to n, find
# any integer y such that p(p(y)) == x and keep a history of the values of y in a return array.
import math
import os
import random
import re
import sys


def permutationEquation(p):
    res = []
    for i in range(1, len(p) + 1):
        x = p.index(i) + 1
        y = p.index(x) + 1
        res.append(y)
    return res
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
