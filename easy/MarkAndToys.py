# https://www.hackerrank.com/challenges/mark-and-toys/problem
# You are given an integer list representing prices for different toys and also
# a total sum of money. What is the maximum number of toys you can buy with the
# money you have?
import math
import os
import random
import re
import sys


def maximumToys(prices, k):
    prices.sort()
    max_price = 0
    res = 0
    
    for price in prices:
        max_price += price
        if max_price <= k:
            res += 1
        else:
            break
            
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
  
