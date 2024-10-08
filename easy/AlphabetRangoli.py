# https://www.hackerrank.com/challenges/alphabet-rangoli/problem
# You are given an integer, N. Your task is to print an alphabet rangoli of size N. 
# (Rangoli is a form of Indian folk art based on creation of patterns.)
# Different sizes of alphabet rangoli are shown below:
# #size 3
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----
import string
import math
import os
import random
import re
import sys


def print_rangoli(size):
    letters = string.ascii_lowercase
    width = 2 * (size + (size-2))+1
    rangoli_list = []
    for i in range(size):
        s = '-'.join(letters[size-1:i:-1] + letters[i:size])
        rangoli_list.append(s.center(width, '-'))
    reverse_rang = rangoli_list[::-1]
    reverse_rang.pop()
    res = reverse_rang + rangoli_list
    for line in res:
        print(line)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
