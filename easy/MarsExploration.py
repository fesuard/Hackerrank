# A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help. 
# Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given 
# the signal received by Earth as a string s, determine how many letters of the SOS message have 
# been changed by radiation.
import math
import os
import random
import re
import sys


def marsExploration(s):
    res = 0
    
    for i in range(0, len(s), 3):
        if 'SOS' != s[i:i+3]:
            if s[i:i+3][0] != 'S':
                res += 1
            if s[i:i+3][1] != 'O':
                res += 1
            if s[i:i+3][2] != 'S':
                res += 1
                
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
