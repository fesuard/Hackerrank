# https://www.hackerrank.com/challenges/most-commons/problem Given a string S,
# which is the company name in lowercase letters, your task is to find the top 
# three most common characters in the string. Print the three most common 
# characters along with their occurrence count. If the occurrence count is the
# same, sort the characters in alphabetical order. 
import math
import os
import random
import re
import sys


# hashmap
def company_logo(s):
    hashm = {}
    for char in s:
        hashm[char] = hashm.get(char, 0) + 1
    sorted_chars = sorted(hashm.items(), key=lambda x: (-x[1], x[0]))
    for s in sorted_chars[:3]:
        print(f'{s[0]} {s[1]}')
    

# using set and count
def company_logo1(s):
    s_count = []
    for char in set(s):
        s_count.append((s.count(char), char))
    s_sorted = sorted(s_count, key=lambda x: (-x[0], x[1]))[:3]
    for s in s_sorted:
        print(f'{s[1]} {s[0]}')


if __name__ == '__main__':
    s = input()
    company_logo(s)
