import math
import os
import random
import re
import sys


def bigSorting(unsorted):
    
    sorted_by_length = sorted(unsorted, key=lambda x: (len(x), int(x)))
            
    return sorted_by_length


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
