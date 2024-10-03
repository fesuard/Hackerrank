# https://www.hackerrank.com/challenges/mini-max-sum/problem
# Given five positive integers, find the minimum and maximum values that can be calculated by summing 
# exactly four of the five integers. Then print the respective minimum and maximum values as a single 
# line of two space-separated long integers.Print two space-separated integers on one line: the minimum 
# sum and the maximum sum of  of  elements.

def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[0:-1]), sum(arr[1:]))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
