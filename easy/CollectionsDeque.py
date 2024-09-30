# https://www.hackerrank.com/challenges/py-collections-deque/problem
# Perform append, pop, popleft and appendleft methods on an empty deque d.
# Input Format
# The first line contains an integer n the number of operations.
# The next n lines contains the space separated names of methods and their values.
# Output Format
# Print the space separated elements of deque d.
from collections import deque


d = deque()
for _ in range(int(input())):
    imp = input().split()
    if len(imp) > 1:
        getattr(d, imp[0])(imp[1])
    else:
        getattr(d, imp[0])()
res = ''
for elem in d:
    res += elem + ' '
print(res)
