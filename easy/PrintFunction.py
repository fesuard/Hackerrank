# https://www.hackerrank.com/challenges/python-print/problem
# The included code stub will read an integer n, from STDIN.
# Without using any string methods, try to print the string:
# 123...n


if __name__ == '__main__':
    n = int(input())
    res = ''
    for i in range(1, n+1):
        res += str(i)
    print (res)
