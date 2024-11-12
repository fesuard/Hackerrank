# insertionSort2 has the following parameter(s):
#     int n: the length of arr
#     int arr[n]: an array of integers
# Prints
# At each iteration, print the array as space-separated integers on its own line.
# Input Format
# The first line contains an integer n the size of arr.
# The next line contains n space-separated integers arr[i]. 


import math
import os
import random
import re
import sys


def insertionSort2(n, arr):
    for i in range(1, n):
        key = arr[i]
        j = i
        
        while j > 0 and arr[j-1] > key:
            arr[j] = arr[j-1]
            j -= 1
            
        arr[j] = key
        print(*arr)
        
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
