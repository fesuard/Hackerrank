# https://www.hackerrank.com/challenges/taum-and-bday/problem
# You have to buy b black gifts and w white gifts. The cost of each black gift is bc units.
# The cost of every white gift is wc units. The cost to convert a black gift into white gift
# or vice versa is z units. Determine the minimum cost of the gifts. 
import math
import os
import random
import re
import sys


def taumBday(b, w, bc, wc, z):
    if bc > wc + z:
        return w * wc + b * wc + z * b
      
    if wc > bc + z:
        return b * bc + w * bc + z * w
      
    return b * bc + w * wc

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()
