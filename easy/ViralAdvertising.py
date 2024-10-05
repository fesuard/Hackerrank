# https://www.hackerrank.com/challenges/strange-advertising/problem
# On the first day, half of those 5 people (5//2=2) like the advertisement and each shares it with 3 of their friends. 
# At the beginning of the second day, 5//2 * 3 people receive the advertisement. Each day, recipients//2 of the recipients 
# like the advertisement and will share it with 3 friends on the following day. Assuming nobody receives the advertisement 
# twice, determine how many people have liked the ad by the end of a given day, beginning with launch day as day 1.
import math
import os
import random
import re
import sys


def viralAdvertising(n):
    shared = 5
    liked = 2
    for i in range(n-1):
        shared = shared // 2 * 3
        liked += shared // 2
    return liked


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
