# https://www.hackerrank.com/challenges/marcs-cakewalk/problem
# You are given a list of calories counts, and you have to calculate the minimum
# number of miles you must run to maintain your current weight. If you have eaten
# j cupcakes so far, after eating a cupcake with c calories you must walk at least
# 2 ** j * c miles to maintain your weight.
import math
import os
import random
import re
import sys


def marcsCakewalk(calorie):
    res = 0
    sorted_cal = sorted(calorie, reverse=True)
    
    for i in range(len(sorted_cal)):
        res += 2 ** i * sorted_cal[i]
        
    return res 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    calories = list(map(int, input().strip().split()))

    result = marcsCakewalk(calories)

    fptr.write(str(result))

    fptr.close()

