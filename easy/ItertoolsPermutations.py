# https://www.hackerrank.com/challenges/itertools-permutations/problem
# You are given a string S.
# Your task is to print all possible permutations of size k of the string S in lexicographic sorted order.
from itertools import permutations


if __name__ == '__main__':
    s, k = input().split()
    k = int(k)
    s = "".join(sorted(s))
    for p in permutations(s, k):
        print("".join(p))
