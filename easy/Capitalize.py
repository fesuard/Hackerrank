# https://www.hackerrank.com/challenges/capitalize/problem
# You are asked to ensure that the first and last names of people begin with a capital letter
# in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
# Given a full name, your task is to capitalize the name appropriately.
import math
import os
import random
import re
import sys


def solve(s):
    res = []
    word_list = s.split()
    for word in word_list:
        word = word.capitalize()
        res.append(word)
    return " ".join(res)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
