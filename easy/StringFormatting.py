# https://www.hackerrank.com/challenges/python-string-formatting/problem
# Given an integer n, print the following values for each integer from 1 to n:
#     Decimal
#     Octal
#     Hexadecimal (capitalized)
#     Binary
# The four values must be printed on a single line in the order specified above for eachfrom each i from 1 to number. Each
# value should be space-padded to match the width of the binary value of number and thevalues should be separated by a 
# single space.

                                              
def print_formatted(number):
    width = len(bin(number)) - 2
    for num in range(1, n+1):
        print(str(num).rjust(width), oct(num)[2:].rjust(width), hex(num)[2:].upper().rjust(width), bin(num)[2:].rjust(width))

                                              
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
