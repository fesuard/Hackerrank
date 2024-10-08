# https://www.hackerrank.com/challenges/day-of-the-programmer/problem
# Marie invented a Time Machine and wants to test it by time-traveling to visit Russia on the 
# Day of the Programmer (the 256th day of the year) during a year in the inclusive range from 1700 to 2700. 
# Given a year y, find the date of the 256th day of that year according to the official Russian calendar 
# during that year.Then print it in the format dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit
# month, and yyyy is y.
import math
import os
import random
import re
import sys


def dayOfProgrammer(year):
    if year >= 1700 and year <= 1917:
        if year % 4 == 0:
            return f'12.09.{year}'
        else:
            return f'13.09.{year}'
    elif year == 1918:
        return f'26.09.1918'
    else:
        if year % 400 == 0 or ((year % 4 == 0) and (year % 100 != 0)):
            return f'12.09.{year}'
        else:
            return f'13.09.{year}'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
