# https://www.hackerrank.com/challenges/time-conversion/problem
# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.
# timeConversion has the following parameter(s):
# string s: a time in 12 hour format
# Returns
# string: the time in 24 hour format
import math
import os
import random
import re
import sys


def timeConversion(s):
    ampm = s[-2:]
    res = ""
    format_hour = 0
    if ampm == "PM":
        hour = int(s[:2])
        if hour < 12:
            format_hour = 12 + hour
            res += str(format_hour) + s[2:-2]
            return res
        elif hour == 12:
            return s[:-2]
    else:
        hour = int(s[:2])
        if hour == 12:
            res += "00" + s[2:-2]
            return res
        else:
            res = s[:-2]
            return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
    
