# https://www.hackerrank.com/challenges/np-arrays/problem
# You are given a space separated list of numbers.
# Your task is to print a reversed NumPy array with the element type float.
import numpy


def arrays(arr):
    rev = arr[::-1]
    res = numpy.array(rev, float)
    return res


if __name__ == '__main__':
    arr = input().strip().split()
    result = arrays(arr)
    print(result)
