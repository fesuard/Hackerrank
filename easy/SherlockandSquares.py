# https://www.hackerrank.com/challenges/sherlock-and-squares/problem
# Watson likes to challenge Sherlock's math ability. He will provide a starting and ending value that describe a 
# range of integers, inclusive of the endpoints. Sherlock must determine the number of square integers within that range.
import math
import os
import random
import re
import sys


def squares(a, b):
    return math.floor(math.sqrt(b)) - math.floor(math.sqrt(a-1))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
