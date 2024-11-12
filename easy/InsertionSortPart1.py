# Given a sorted list with an unsorted number e in the rightmost cell, can you write some 
# simple code to insert e into the array so that it remains sorted? Assume you are given the 
# array arr = [1, 2, 4, 5, 3], indexed 0..4. Store the value of arr[4]. Now test lower index 
# values successively from 3 to 0 until you reach a value that is lower than arr[4], at arr[1]
# in this case. Each time your test fails, copy the value at the lower index to the current
# index and print your array. When the next lower indexed value is smaller than arr[4], insert
# the stored value at the current index and print the entire array.
import math
import os
import random
import re
import sys


def insertionSort1(n, arr):
    key = arr[-1]
    i = n - 1
    
    while i > 0 and arr[i-1] > key:
        arr[i] = arr[i-1]
        i -= 1
        print(*arr)
        
    arr[i] = key
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
