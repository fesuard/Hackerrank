# Staircase detail
# This is a staircase of size n=4:
   #
  ##
 ###
####
# Its base and height are both equal to n. It is drawn using # symbols and spaces. The last line is not preceded by any spaces.
# Write a program that prints a staircase of size n.

def staircase(n):
    for i in range(1, n+1):
        txt = i * "#"
        print(txt.rjust(n)) 


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
