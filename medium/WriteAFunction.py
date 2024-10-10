# https://www.hackerrank.com/challenges/write-a-function/problem
# Given a year, determine whether it is a leap year. If it is a leap year, return the
# Boolean True, otherwise return False.


def is_leap(year):
    leap = False
    if year % 4 == 0 and (year % 100 != 0) or (year % 400 == 0):
        leap = True
    return leap
