# The task is to determine if it's possible for all ladybugs to be happy.A ladybug is 
# considered happy if it is adjacent to at least one other ladybug of the same type.
# An underscore (_) in the string represents an empty space, which allows movement.
import math
import os
import random
import re
import sys


def happyLadybugs(b):
    n = len(b)
    hashm = {}
    
    for letter in b:
        if letter.isupper():
            hashm[letter] = hashm.get(letter, 0) + 1
        else:
            hashm['unders'] = hashm.get('unders', 0) + 1
            
    if hashm.get('unders', 0) > 0:
        for key, value in hashm.items():
            if key != 'unders' and value == 1:
                return 'NO'
        return 'YES'
                
    else:
        for value in hashm.values():
            if value == 1:
                return 'NO'
            
        for i in range(1, len(b) - 1):
            if b[i] != b[i-1] and b[i] != b[i+1]:
                return 'NO'
                
        return 'YES'            
        
                  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
