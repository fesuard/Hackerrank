# https://www.hackerrank.com/challenges/priyanka-and-toys/problem
# Priyanka works for an international toy company that ships by container. Her task
# is to the determine the lowest cost way to combine her orders for shipping. She 
# has a list of item weights. The shipping company has a requirement that all items 
# loaded in a container must weigh less than or equal to 4 units plus the weight of 
# the minimum weight item. All items meeting that requirement will be shipped in one
# container.
# What is the smallest number of containers that can be contracted to ship the items
# based on the given list of weights?
import math
import os
import random
import re
import sys


def toys(w):
    w.sort()
    res = 0
    n = len(w)
    i = 0
    j = 1
    
    while j < n:
        if w[i] + 4 >= w[j]:
            if j == n - 1:
                res += 1
            j += 1
                  
        else:
            res += 1
            i = j
            j += 1
        
    if w[-1] > w[-2] + 4:
        res += 1
            
    return res

# same approach but better written and the edge cases are handled directly
def toys1(w):
    w.sort()
    res = 0
    n = len(w)
    i = 0
    
    while i < n:
        res += 1
        current_weight = w[i]
        i += 1
        
        while i < n and w[i] <= current_weight + 4:
            i += 1
    
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()

