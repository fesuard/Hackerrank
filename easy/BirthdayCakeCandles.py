# https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true
# You are in charge of the cake for a child's birthday. You have decided the cake will have 
# one candle for each year of their total age. They will only be able to blow out the tallest
# of the candles. Count how many candles are tallest.
# Function Description
# Complete the function birthdayCakeCandles in the editor below.
# birthdayCakeCandles has the following parameter(s):
# int candles[n]: the candle heights
import math
import os
import random
import re
import sys


# using count
def birthdayCakeCandles(candles):
    tallest = max(candles)
    return candles.count(tallest)

# hashmap
def birthdayCakeCandles1(candles):
    hashm = {}
    for candle in candles:
        hashm[candle] = hashm.get(candle, 0) + 1
    return hashm[max(hashm.keys())]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()
