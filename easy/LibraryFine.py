# https://www.hackerrank.com/challenges/library-fine/problem
# Given the expected and actual return dates for a library book, create a program that
# calculates the fine (if any). The fee structure is as follows:
# If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0)
# If the book is returned after the expected return day but still within the same calendar month and year
# as the expected return date: fine = 15 * (numbers of days late)
# If the book is returned after the expected return month but still within the same calendar year as the 
# expected return date: fine = 500 * (numbers of months late)
# If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000.
import math
import os
import random
import re
import sys


def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return 10000
        
    if m1 > m2 and y1 == y2:
        return (m1 - m2) * 500
        
    if d1 > d2 and m1 == m2 and y1 == y2:
        return (d1 - d2) * 15
        
    return 0
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
