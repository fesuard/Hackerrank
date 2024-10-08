# https://www.hackerrank.com/challenges/electronics-shop/problem
# A person wants to determine the most expensive computer keyboard and USB drive that can be 
# purchased with a give budget. Given price lists for keyboards and USB drives and a budget, 
# find the cost to buy them. If it is not possible to buy both items, return -1.
import math
import os
import random
import re
import sys


def getMoneySpent(keyboards, drives, b):
    prices = []
    for k in keyboards:
        for d in drives:
            if k + d <= b:
                prices.append(k+d)
    if len(prices) > 0:
        return max(prices)
    else:
        return -1
             
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    bnm = input().split()
    
    b = int(bnm[0])
    
    n = int(bnm[1])
    
    m = int(bnm[2])
    
    keyboards = list(map(int, input().rstrip().split()))
    
    drives = list(map(int, input().rstrip().split()))
    
    moneySpent = getMoneySpent(keyboards, drives, b)
    
    fptr.write(str(moneySpent) + '\n')
    
    fptr.close()
