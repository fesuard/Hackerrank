# https://www.hackerrank.com/challenges/bon-appetit/problem
# Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will 
# only pay for the items they consume. Brian gets the check and calculates Anna's portion.
# You must determine if his calculation is correct. Complete the bonAppetit function in 
# the editor below. It should print Bon Appetit if the bill is fairly split. Otherwise,
# it should print the integer amount of money that Brian owes Anna.
# bonAppetit has the following parameter(s):
#     bill: an array of integers representing the cost of each item ordered
#     k: an integer representing the zero-based index of the item Anna doesn't eat
#     b: the amount of money that Anna contributed to the bill
import math
import os
import random
import re
import sys


def bonAppetit(bill, k, b):
    bill.pop(k)
    split_bill = int(sum(bill)/2)
    if split_bill == b:
        print("Bon Appetit")
    else:
        print(b - split_bill)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
