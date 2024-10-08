# https://www.hackerrank.com/challenges/python-sort-sort/problem
# You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and so on). 
# You are required to sort the data based on the Kth attribute and print the final resulting table. 
# Note that K is indexed from 0 to M-1, where M is the number of attributes.
# Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, 
# print the row that appeared first in the input.


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())

    sorted_arr = sorted(arr, key=lambda x: x[k])

    for arr in sorted_arr:
        print(*arr)
