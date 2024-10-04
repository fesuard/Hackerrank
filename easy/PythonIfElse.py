# https://www.hackerrank.com/challenges/py-if-else/problem
# Given an integer n, perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
import math
import os
import random
import re
import sys


def even_odd(n):
    if n % 2 != 0:
        print('Weird')
    elif n % 2 == 0 and 2 <= n <= 5:
        print('Not Weird')
    elif n % 2 == 0 and 6 <= n <= 20:
        print('Weird')
    elif n % 2 == 0 and n > 20:
        print('Not Weird')


if __name__ == '__main__':
    n = int(input().strip())
    even_odd(n)
