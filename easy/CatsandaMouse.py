# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
# Two cats and a mouse are at various positions on a line. You will be given their starting
# positions. Your task is to determine which cat will reach the mouse first, assuming the 
# mouse does not move and the cats travel at equal speed. If the cats arrive at the same time,
# the mouse will be allowed to move and it will escape while they fight.
import math
import os
import random
import re
import sys


def catAndMouse(x, y, z):
    if abs(x-z) > abs(y-z):
        return 'Cat B'
    elif abs(x-z) < abs(y-z):
        return 'Cat A'
    else:
        return 'Mouse C'


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])
        result = catAndMouse(x, y, z)
        f.write(result + '\n')
    f.close()
