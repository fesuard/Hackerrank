# There is a collection of rocks where each rock has various minerals embeded in it. Each
# type of mineral is designated by a lowercase letter in the range ascii[a-z]. There may 
# be multiple occurrences of a mineral in a rock. A mineral is called a gemstone if it 
# occurs at least once in each of the rocks in the collection. Given a list of minerals
# embedded in each of the rocks, display the number of types of gemstones in the collection.
import math
import os
import random
import re
import sys


def gemstones(arr):
    hashm = {}
    res = 0
    set_arr = [set(elem) for elem in arr]
    
    for elem in set_arr:
        for char in elem:
            hashm[char] = hashm.get(char, 0) + 1
    
    for value in hashm.values():
        if value == len(arr):
            res += 1
    
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
