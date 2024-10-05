# https://www.hackerrank.com/challenges/itertools-product/problem
# You are given a two lists A and B.
# Your task is to compute their cartesian product AXB.
from itertools import product


if __name__ == '__main__':
    lst_a = map(int, input().split())
    lst_b = map(int, input().split())
    
    print(*list(product(lst_a, lst_b)))
