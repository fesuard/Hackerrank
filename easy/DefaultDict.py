# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
# In this challenge, you will be given 2 integers n, and m. There are words, which might repeat, in word
# group A. There are m words belonging to word group B. For each m words, check whether the word has appeared
# in group A or not. Print the indices of each occurrence of m in group A. If it does not appear, print -1.
from collections import defaultdict


if __name__ == '__main__':
    n, m = map(int, input().split())
    group_a = []
    group_b = []
    for _ in range(n):
        group_a.append(input())
    for _ in range(m):
        group_b.append(input())
    dic_a = defaultdict(list)
    for index, elem in enumerate(group_a):
        dic_a[elem].append(str(index+1))
    for elem in group_b:
        if elem in dic_a:
            print(' '.join(dic_a[elem]))
        else:
            print('-1')
