# https://www.hackerrank.com/challenges/jim-and-the-orders/problem
# Jim's Burgers has a line of hungry customers. Orders vary in the time it takes to
# prepare them. Determine the order the customers receive their orders. Start by
# numbering each of the customers from 1 to n, front of the line to the back. You 
# will then be given an order number and a preparation time for each customer. 
# The time of delivery is calculated as the sum of the order number and the
# preparation time. If two orders are delivered at the same time, assume they are 
# delivered in ascending customer number order.
import math
import os
import random
import re
import sys


def jimOrders(orders):
    res = []
    for i in range(len(orders)):
        orders[i].append(i + 1)
        
    sorted_orders = sorted(orders, key=lambda x: (x[0] + x[1], x[2]))
    
    for order in sorted_orders:
        res.append(order[2])
        
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
