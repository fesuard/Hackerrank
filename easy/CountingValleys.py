# https://www.hackerrank.com/challenges/counting-valleys/problem
# An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly steps, 
# for every step it was noted if it was an uphill, , or a downhill, step. Hikes always start and end at
# sea level, and each step up or down represents a unit change in altitude. We define the following terms:
#     A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level
# and ending with a step down to sea level.
#     A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level
# and ending with a step up to sea level.
import math
import os
import random
import re
import sys


def countingValleys(steps, path):
    level = 0
    res = 0
    for step in path:
        if step == 'U':
            level += 1
            if level == 0:
                res += 1
        else:
            level -= 1
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
