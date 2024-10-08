# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given n scores. Store them in a list and find the score of the runner-up.
import math
import os
import random
import re
import sys


#using sort():
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sorted_arr = list(set(arr))
    sorted_arr.sort()
    print(sorted_arr[-2])

#manually getting the biggest 2 values:
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    biggest_value = runner_up = float('-inf')
    arr_list = list(set(arr))
    for elem in arr_list:
        if elem >= biggest_value:
            biggest_value, runner_up = elem, biggest_value
        elif elem < biggest_value:
            runner_up = max(runner_up, elem)
    print(runner_up)
