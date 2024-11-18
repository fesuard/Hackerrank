# https://www.hackerrank.com/challenges/pangrams/problem
# A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether
# it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.
import math
import os
import random
import re
import sys


def pangrams(s):
    alpha_list = [
      'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
      't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

    for letter in s:
        if letter.isalpha():
            letter = letter.lower()
            if letter in alpha_list:
                alpha_list.remove(letter)
    
    if alpha_list:
        return 'not pangram'
    else:
        return 'pangram'
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
