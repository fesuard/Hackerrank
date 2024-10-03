# https://www.hackerrank.com/challenges/plus-minus/problem
# Given an array of integers, calculate the ratios of its elements that are positive, negative,
# and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.
# Complete the plusMinus function in the editor below.Print the ratios of positive, negative and 
# zero values in the array. Each value should be printed on a separate line with  digits after the
# decimal. The function should not return a value.


def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    n = len(arr)
    for elem in arr:
        if elem > 0:
            positive += 1
        elif elem < 0:
            negative += 1
        else:
            zero += 1
    print(f'{positive/n:.6f}')
    print(f'{negative/n:.6f}')
    print(f'{zero/n:.6f}')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
