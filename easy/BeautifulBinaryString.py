# https://www.hackerrank.com/challenges/beautiful-binary-string/problem
# Alice has a binary string. She thinks a binary string is beautiful if and only if it
# doesn't contain the substring "010". In one step, Alice can change a 0 to a 1 or vice 
# versa. Count and print the minimum number of steps needed to make Alice see the string
# as beautiful.
import math
import os
import random
import re
import sys


def beautifulBinaryString(b):
    return b.count("010")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
