# https://www.hackerrank.com/challenges/designer-door-mat/problem
# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the
# following specifications: Mat size must be N X M. (N is an odd natural number, and M is times bigger 
# than N). The design should have 'WELCOME' written in the center. The design pattern should only use 
# |, . and - characters.


if __name__ == '__main__':
    N,M = map(int, input().split())
    c = '.|.'
    r = N//2
    for i in range(r):
        print((c*i).rjust(M//2-1, '-')+c+(c*i).ljust(M//2-1, '-'))
    print('WELCOME'.center(M, '-'))
    for i in range(r):
        print((c*(r-i-1)).rjust(M//2-1, '-')+c+(c*(r-i-1)).ljust(M//2-1, '-'))
