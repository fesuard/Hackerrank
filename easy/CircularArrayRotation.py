# One rotation operation moves the last array element to the first position and shifts all 
# remaining elements right one. Perform the rotation operation a number of times then
# determine the value of the element at a given position. For each array, perform a number
# of right circular rotations and return the values of the elements at the given indices.
import math
import os
import random
import re
import sys


def circularArrayRotation(a, k, queries):
    res = []
    
    for _ in range(k):
        elem = a.pop()
        a.insert(0, elem)
        
    for q in queries:
        res.append(a[q])
        
    return res
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
