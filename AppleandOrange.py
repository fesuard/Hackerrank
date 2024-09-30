# https://www.hackerrank.com/challenges/apple-and-orange/problem
# Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the
# information given below, determine the number of apples and oranges that land on Sam's house.
# The red region denotes the house, where s is the start point, and t is the endpoint. The apple 
# tree is to the left of the house, and the orange tree is to its right. Assume the trees are 
# located on a single point, where the apple tree is at point a, and the orange tree is at point b.
# When a fruit falls from its tree, it lands d units of distance from its tree of origin along the
# -axis. *A negative  of d means the fruit fell  units to the tree's left, and a positive 
# value of  means it falls d units to the tree's right.
import math
import os
import random
import re
import sys


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_count = 0
    oranges_count = 0
    for d in apples:
        if a + d in range(s, t+1):
            apples_count += 1
    for d in oranges:
        if d + b in range(s, t+1):
            oranges_count += 1
    print(f"{apples_count}\n{oranges_count}")


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
