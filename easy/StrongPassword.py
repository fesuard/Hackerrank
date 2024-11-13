# You need to come up with a password that follows the following rules:
#     Its length is at least 6.
#     It contains at least one digit.
#     It contains at least one lowercase English character.
#     It contains at least one uppercase English character.
#     It contains at least one special character. The special characters are: !@#$%^&*()-+
# What's the minimum numbers of characters to add so that the password is valid?
import math
import os
import random
import re
import sys


def minimumNumber(n, password):
    res = 0
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    check_numbers = False
    check_upper = False
    check_lower = False
    check_special = False
    
    for char in password:
        if char in numbers:
            check_numbers = True
        elif char in lower_case:
            check_lower = True
        elif char in upper_case:
            check_upper = True
        elif char in special_characters:
            check_special = True
    check = sum([check_numbers, check_upper, check_lower, check_special])
            
    if n > 5 and check == 4:
        res = 0
    else:
         if n > 5:
             res = 4 - check
         else:
             res = max(6 - n, 4 - check)
    
    return res
             

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
